from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import Permission
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, FormView

from entrees.forms import RecommendedContactCreationForm, ReferentContactCreationForm
from entrees.models import RecommendedContact



def sign_up(request):
    if request.method == "GET":
        form = ReferentContactCreationForm()
        return render(request, "registration/login.html", {"form": form})
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
            return redirect("fields:index")
        else:
            return render(request, "registration/login.html", {"form": form})
