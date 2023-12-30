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
from django.contrib.auth.models import User
from django.urls import path
from viewflow.urls import Application, ModelViewset, ReadonlyModelViewset, Site

from . import views
from . import models
from . import viewsets

site = Site(
    title="* Annuaire X-UE",
    viewsets=[
        Application(
            title="* Utilisateurs et contacts",
            icon="people",
            app_name="people",
            viewsets=[
                ModelViewset(model=User),
                viewsets.ReferentContactViewset(),
                viewsets.RecommendedContactViewset(),
                viewsets.CustomRecommendedContactViewset(),
            ],
        ),
        Application(
            title="* Domaines de compétence",
            icon="book",
            app_name="fields",
            viewsets=[
                ReadonlyModelViewset(model=models.FieldOfCompetence, icon="book"),
                viewsets.RecommendedContactByFieldViewset(),
            ],
        ),
    ],
)

urlpatterns = [
    path("", site.urls),
    path("register/", views.sign_up, name="register"),
]
