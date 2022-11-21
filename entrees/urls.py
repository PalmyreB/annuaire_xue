from django.urls import path

from . import views

app_name = "entrees"
urlpatterns = [
    path("", views.index, name="index"),
    path(
        "referent/<int:referent_contact_id>/",
        views.referent_contact,
        name="referent_contact",
    ),
    path(
        "recommended/<int:recommended_contact_id>/",
        views.recommended_contact,
        name="recommended_contact",
    ),
    path("field/<str:field_slug>/", views.FieldView.as_view(), name="field"),
    path("form/", views.send_contacts, name="new-contact-form"),
    path("contacts/", views.FieldView.as_view(), name="contacts"),
]
