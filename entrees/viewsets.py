from django.urls import path
from viewflow.urls import ModelViewset, ReadonlyModelViewset, Viewset

from . import forms, models, views


class HomeViewset(Viewset):
    index_path = path("", views.index, name="index")


class ReferentContactViewset(ModelViewset):
    icon = "people"
    model = models.ReferentContact
    list_filter_fields = ["user__first_name", "user__last_name"]
    create_form_class = forms.ReferentContactCreationForm


class RecommendedContactReadOnlyViewset(ReadonlyModelViewset):
    icon = "people"
    model = models.RecommendedContact
    list_columns = (
        "first_name",
        "last_name",
        "list_fields_of_competence",
    )
    list_filter_fields = ["first_name", "last_name", "fields_of_competence"]

    def list_fields_of_competence(self, obj):
        return ", ".join(obj.fields_of_competence.values_list("name", flat=True))

    list_fields_of_competence.short_description = "Domaines de compétence"


class RecommendedContactWithFieldFilterViewset(RecommendedContactReadOnlyViewset):
    title = "Tous les contacts recommandés"


class RecommendedContactByFieldViewset(ReadonlyModelViewset):
    icon = "people"
    model = models.RecommendedContact
    list_columns = (
        "first_name",
        "last_name",
    )
    list_filter_fields = ["first_name", "last_name"]
    create_form_class = forms.RecommendedContactCreationForm
    field = None

    def __init__(self, **kwargs):
        if "field" in kwargs:
            self.field = kwargs.pop("field")
        if self.field:
            if self.namespace:
                self.namespace = f"{self.namespace}:{self.field.slug}"
            else:
                self.namespace = self.field.slug
        super().__init__(**kwargs)

    def get_queryset(self, request):
        """
        Filter contacts by field.
        """
        if self.field:
            return models.RecommendedContact.objects.filter(
                fields_of_competence__id=self.field.id
            )
        else:
            return models.RecommendedContact.objects.all()

    @property
    def index_path(self):
        """
        Add field in URL.
        """
        return path(self.field.slug if self.field else "", self.list_view, name="index")


class RecommendedContactAddedByUserViewset(ModelViewset):
    title = "Mes recommandations"
    icon = "people"
    model = models.RecommendedContact
    list_columns = (
        "first_name",
        "last_name",
        "list_fields_of_competence",
    )
    list_filter_fields = ["first_name", "last_name", "fields_of_competence"]
    # create_form_class = forms.RecommendedContactCreationForm
    create_view_class = views.RecommendedContactCreationView
    # create_view_class = views.ContactFormView
    # create_form_layout = forms.RecommendedContactCreationForm.layout
    update_form_layout = forms.RecommendedContactUpdateForm.layout

    def list_fields_of_competence(self, obj):
        return ", ".join(obj.fields_of_competence.values_list("name", flat=True))

    list_fields_of_competence.short_description = "Domaines de compétence"

    def get_queryset(self, request):
        """
        Filter contacts created by connected user.
        """
        referent_contact = models.ReferentContact.objects.get(user=request.user)
        return models.RecommendedContact.objects.filter(
            referent_contact=referent_contact
        )
