from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from viewflow.forms import FieldSet, Layout, Row

from . import models


class ReferentContactCreationForm(forms.ModelForm):
    username = forms.CharField(label=_("Identifiant"), max_length=200)
    password1 = forms.CharField(
        label=_("Mot de passe"), max_length=30, widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label=_("Confirmation du mot de passe"),
        max_length=30,
        widget=forms.PasswordInput(),
    )
    first_name = forms.CharField(label=_("Prénom"), max_length=200)
    last_name = forms.CharField(label=_("Nom de famille"), max_length=200)
    email = forms.EmailField(label=_("Adresse email"), max_length=200)

    class Meta:
        model = models.ReferentContact
        exclude = ("user",)

    # layout = Layout(
    #     "username",
    #     Row("password1", "password2"),
    #     Row("first_name", "last_name"),
    #     "email",
    #     Row("phone", "city", "promotion"),
    # )

    layout = Layout(
        "username",
        "password1",
        "password2",
        "first_name",
        "last_name",
        "email",
        "phone",
        "city",
        "promotion",
    )

    def clean_username(self):  # check if username does not exist before
        try:
            User.objects.get(
                username=self.cleaned_data["username"]
            )  # get user from user model
        except User.DoesNotExist:
            return self.cleaned_data["username"]

        raise forms.ValidationError("Cet utilisateur existe déjà")

    def clean(self):  # check if password 1 and password2 match each other
        if (
            "password1" in self.cleaned_data and "password2" in self.cleaned_data
        ):  # check if both pass first validation
            if (
                self.cleaned_data["password1"] != self.cleaned_data["password2"]
            ):  # check if they match each other
                raise forms.ValidationError("Les mots de passe ne sont pas identiques")

        return self.cleaned_data

    def save(self):  # create new user
        new_user = User.objects.create_user(
            username=self.cleaned_data["username"],
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            password=self.cleaned_data["password1"],
            email=self.cleaned_data["email"],
        )
        models.ReferentContact.objects.get_or_create(
            user=new_user,
            phone=self.cleaned_data["phone"],
            city=self.cleaned_data["city"],
            promotion=self.cleaned_data["promotion"],
        )

        return new_user


class RecommendedContactCreationForm(forms.ModelForm):
    has_approved = forms.BooleanField(
        label=_(
            "Je confirme que je m'engage à servir d'intermédiaire pour mettre en relation des personnes d'X-UE avec ce contact."
        )
    )
    has_informed = forms.BooleanField(
        label=_(
            "Je confirme que mon contact est informé qu'il figurera dans cet annuaire."
        )
    )

    class Meta:
        model = models.RecommendedContact
        exclude = ("referent_contact",)

    layout = Layout(
        FieldSet(
            "Coordonnées personnelles",
            Row("first_name", "last_name"),
            "website",
        ),
        FieldSet(
            "Engagement",
            Row("structure", "function"),
            "engagements",
            "reasons_to_contact",
            "fields_of_competence",
            "other_fields_of_competence",
        ),
        FieldSet(
            "Confirmation",
            Row("has_approved", "has_informed"),
        ),
    )


class RecommendedContactUpdateForm(forms.ModelForm):
    class Meta:
        model = models.RecommendedContact
        exclude = ("referent_contact",)

    layout = Layout(
        FieldSet(
            "Coordonnées personnelles",
            Row("first_name", "last_name"),
            "website",
        ),
        FieldSet(
            "Engagement",
            Row("structure", "function"),
            "engagements",
            "reasons_to_contact",
            "fields_of_competence",
            "other_fields_of_competence",
        ),
    )


class RecommendedContactViewForm(forms.ModelForm):
    class Meta:
        model = models.RecommendedContact
        fields = "__all__"

    layout = Layout(
        FieldSet(
            "Coordonnées personnelles",
            Row("first_name", "last_name"),
            "website",
            "referent_contact",
        ),
        FieldSet(
            "Engagement",
            Row("structure", "function"),
            "engagements",
            "reasons_to_contact",
            "fields_of_competence",
            "other_fields_of_competence",
        ),
    )
