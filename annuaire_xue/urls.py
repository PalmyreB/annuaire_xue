"""
URL configuration for annuaire_xue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from viewflow.contrib.auth import AuthViewset
from viewflow.urls import Application, ModelViewset, ReadonlyModelViewset, Site

from entrees import models as entrees_models
from entrees import viewsets as entrees_viewsets

site = Site(
    title="Annuaire X-UE",
    viewsets=[
        Application(
            title="Utilisateurs et contacts",
            icon="people",
            app_name="people",
            viewsets=[
                ModelViewset(model=User),
                entrees_viewsets.ReferentContactViewset(),
                entrees_viewsets.RecommendedContactViewset(),
            ],
        ),
        Application(
            title="Domaines de compétence",
            icon="book",
            app_name="fields",
            viewsets=[
                ReadonlyModelViewset(
                    model=entrees_models.FieldOfCompetence, icon="book"
                ),
            ],
        ),
    ],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", AuthViewset(with_profile_view=True).urls),
    path("entrees/", include(("entrees.urls", "entrees"))),
    path("", site.urls),
]
