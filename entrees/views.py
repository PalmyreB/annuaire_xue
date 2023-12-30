from django.contrib.auth import login
from django.contrib.auth.models import Permission
from django.contrib.auth.views import LoginView as BaseLoginView
from django.shortcuts import render
from django.views.generic.edit import CreateView

from entrees.forms import RecommendedContactCreationForm, ReferentContactCreationForm
from entrees.models import RecommendedContact, ReferentContact


class RecommendedContactCreationView(CreateView):
    model = RecommendedContact
    template_name = "viewflow/views/form.html"
    form_class = RecommendedContactCreationForm
    success_url = "/people/recommended_contact/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        instance = form.save(commit=False)
        instance.referent_contact = ReferentContact.objects.get(user=self.request.user)
        instance.save()
        return super().form_valid(form)


def sign_up(request):
    if request.method == "GET":
        form = ReferentContactCreationForm()
        return render(request, "entrees/register.html", {"form": form})
    if request.method == "POST":
        form = ReferentContactCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            # TODO: Put list of permissions elsewhere (settings ? .env ?)
            permissions = Permission.objects.filter(
                codename__in=[
                    "view_fieldofcompetence",
                    "add_recommendedcontact",
                    "change_recommendedcontact",
                    "delete_recommendedcontact",
                    "view_recommendedcontact",
                    "view_referentcontact",
                ]
            )
            user.user_permissions.add(*permissions)
            login(request, user)
            return index(request)
        else:
            return render(request, "entrees/register.html", {"form": form})


def index(request):
    return render(request, "entrees/home.html")


class LoginView(BaseLoginView):
    template_name = "entrees/login.html"
