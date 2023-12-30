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
from django.urls import include, path
from viewflow.contrib.auth import AuthViewset
from viewflow.urls import Site

from entrees import applications as entrees_applications
from entrees import views as entrees_views

site = Site(
    title="Annuaire X-UE",
    primary_color="#003e5c",
    secondary_color="#d52b1e",
    viewsets=[
        entrees_applications.HomeApplication(),
        entrees_applications.PeopleApplication(),
        entrees_applications.FieldsApplication(),
    ],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", entrees_views.LoginView.as_view()),
    path("accounts/register/", entrees_views.sign_up, name="register"),
    path("accounts/", AuthViewset(with_profile_view=True).urls),
    path("entrees/", include(("entrees.urls", "entrees"))),
    path("", site.urls),
]
