from django.urls import path

from . import views
from .forms import RecommendedContactForm, ReferentContactForm

app_name = "entrees"
urlpatterns = [
    path("", views.index, name="index"),
    path(
        "referent/<int:referent_contact_id>/",
        views.referent_contact_view,
        name="referent-contact",
    ),
    path(
        "recommended/<int:pk>/",
        views.RecommendedContactDetailView.as_view(),
        name="recommended-contact",
    ),
    path(
        "field/<str:field_of_competence_slug>/",
        views.FieldOfCompetenceView.as_view(),
        name="field-of-competence",
    ),
    path("form/", views.send_contacts, name="new-contact-form"),
    path("contacts/", views.FieldOfCompetenceView.as_view(), name="contacts"),
    path("new-contact/", views.ContactWizard.as_view(), name="new-contact"),
]
