import django_filters
import django_tables2 as tables
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext as _
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from .forms import RecommendedContactFormset, ReferentContactForm
from .models import FieldOfCompetence, RecommendedContact, ReferentContact


def index(request):
    latest_referent_contact_list = ReferentContact.objects.order_by(
        "-registration_date"
    )[:5]
    field_list = FieldOfCompetence.objects.all()
    context = {
        "latest_referent_contact_list": latest_referent_contact_list,
        "field_list": field_list,
    }
    # return render(request, "material/frontend/base.html", context)
    return render(request, "entrees/index.html", context)


def referent_contact(request, referent_contact_id):
    try:
        contact = ReferentContact.objects.get(pk=referent_contact_id)
    except ReferentContact.DoesNotExist:
        raise Http404(_("Ce contact n'existe pas."))
    return HttpResponse(
        _("Vous regardez le contact référent %s : %s." % (referent_contact_id, contact))
    )


def recommended_contact(request, recommended_contact_id):
    try:
        contact = ReferentContact.objects.get(pk=recommended_contact_id)
    except ReferentContact.DoesNotExist:
        raise Http404(_("Ce contact n'existe pas."))
    return HttpResponse(
        _("Vous regardez le contact recommandé %s." % recommended_contact_id)
    )


def send_contacts(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ReferentContactForm(request.POST)
        formset = RecommendedContactFormset(request.POST)
        # check whether it's valid:
        if form.is_valid() and formset.is_valid():
            # process the data in form.cleaned_data as
            referent_contact_data = form.cleaned_data
            referent_contact_data["registration_date"] = now()
            referent_contact = ReferentContact(**referent_contact_data)
            referent_contact.save()

            for current_form in formset:
                recommended_contact_data = current_form.cleaned_data
                # Manage many-to-many relationships
                fields_of_competence = recommended_contact_data.pop(
                    "fields_of_competence", []
                )
                # Manage additional fields
                recommended_contact_data.pop("has_approved", None)
                recommended_contact_data.pop("has_informed", None)

                recommended_contact_data["referent_contact"] = referent_contact
                recommended_contact = RecommendedContact(**recommended_contact_data)
                recommended_contact.save()
                recommended_contact.fields_of_competence.set(fields_of_competence)

            # redirect to a new URL:
            return HttpResponseRedirect(reverse("entrees:index"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReferentContactForm()
        formset = RecommendedContactFormset()

    return render(request, "entrees/form.html", {"form": form, "formset": formset})


class RecommendedContactsTable(tables.Table):
    fields_of_competence = tables.ManyToManyColumn(
        transform=lambda field_of_competence: field_of_competence.name
    )

    class Meta:
        model = RecommendedContact


class AllContactsView(tables.SingleTableView):
    table_class = SimpleTable
    queryset = RecommendedContact.objects.all()
    template_name = "entrees/table.html"


class FieldOfCompetenceFilter(django_filters.FilterSet):
    class Meta:
        model = RecommendedContact
        fields = ["firstname", "lastname", "fields_of_competence"]


class FieldOfCompetenceView(SingleTableMixin, FilterView):
    """
    Table view of recommended contacts with filters

    On the page of a specific field, only the queryset of contacts having this field is shown.
    """

    table_class = RecommendedContactsTable
    model = RecommendedContact
    template_name = "entrees/table.html"
    filterset_class = FieldOfCompetenceFilter

    def get_queryset(self):
        if "field_of_competence_slug" in self.kwargs:
            return RecommendedContact.objects.filter(
                fields_of_competence__slug=self.kwargs["field_of_competence_slug"]
            )
