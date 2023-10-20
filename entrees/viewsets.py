from viewflow.urls import ModelViewset

from . import forms, models


class ReferentContactViewset(ModelViewset):
    icon = "people"
    model = models.ReferentContact
    # list_columns = ("")
    list_filter_fields = ["user__first_name", "user__last_name"]
    create_form_class = forms.ReferentContactCreationForm


class RecommendedContactViewset(ModelViewset):
    icon = "people"
    model = models.RecommendedContact
    # list_columns = ("first_name", "last_name", "fields_of_competence",)
    list_filter_fields = ["first_name", "last_name", "fields_of_competence"]
    create_form_class = forms.RecommendedContactForm
