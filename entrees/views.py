from django.shortcuts import render
from django.views.generic.edit import CreateView

from entrees.forms import RecommendedContactCreationForm
from entrees.models import RecommendedContact, ReferentContact


class RecommendedContactCreationView(CreateView):
    model = RecommendedContact
    template_name = "viewflow/views/form.html"
    form_class = RecommendedContactCreationForm
    success_url = "/people/recommended_contact_added_by_user/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        instance = form.save(commit=False)
        instance.referent_contact = ReferentContact.objects.get(user=self.request.user)
        instance.save()
        return super().form_valid(form)


def index(request):
    return render(request, "entrees/home.html")
