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

from contacts import applications as contacts_applications
from accounts import views as accounts_views

site = Site(
    title="Annuaire X-UE",
    primary_color="#003e5c",
    secondary_color="#d52b1e",
    viewsets=[
        contacts_applications.HomeApplication(),
        contacts_applications.PeopleApplication(),
        contacts_applications.FieldsApplication(),
    ],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", accounts_views.LoginView.as_view()),
    path("accounts/register/", accounts_views.sign_up, name="register"),
    path("accounts/", AuthViewset(with_profile_view=True).urls),
    path("contacts/", include(("contacts.urls", "contacts"))),
    path("", site.urls),
]
