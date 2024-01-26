from django.contrib.auth import login
from django.contrib.auth.models import Permission
from django.contrib.auth.views import LoginView as BaseLoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from contacts import forms as contacts_forms


def sign_up(request):
    if request.method == "POST":
        form = contacts_forms.ReferentContactCreationForm(request.POST)
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
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "accounts/register.html", {"form": form})
    else:  # if request.method == "GET":
        form = contacts_forms.ReferentContactCreationForm()
        return render(request, "accounts/register.html", {"form": form})


class LoginView(BaseLoginView):
    template_name = "accounts/login.html"
