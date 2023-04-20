from django.forms import BooleanField, ModelForm, formset_factory, inlineformset_factory
from django.utils.translation import gettext as _
from material import Layout, Row

from .models import RecommendedContact, ReferentContact


class ReferentContactForm(ModelForm):
    prefix = "referent"

    class Meta:
        model = ReferentContact
        fields = ["first_name", "last_name", "mail", "phone", "city", "promotion"]

    layout = Layout(
        Row("first_name", "last_name"), "mail", Row("phone", "city", "promotion")
    )


class RecommendedContactForm(ModelForm):
    prefix = "recommended"
    has_approved = BooleanField(
        label=_(
            "Je confirme que je m'engage à servir d'intermédiaire pour mettre en relation des personnes d'X-UE avec ce contact."
        ),
    )
    has_informed = BooleanField(
        label=_(
            "Je confirme que mon contact secondaire est informé qu'il figurera dans cet annuaire. "
        ),
    )

    class Meta:
        model = RecommendedContact
        fields = [
            "first_name",
            "last_name",
            "website",
            "structure",
            "function",
            "engagements",
            "reasons_to_contact",
            "fields_of_competence",
            "other_fields_of_competence",
        ]

    layout = Layout(
        Row("first_name", "last_name"),
        "website",
        Row("structure", "function"),
        "engagements",
        "reasons_to_contact",
        "fields_of_competence",
        "other_fields_of_competence",
        Row("has_approved", "has_informed"),
        "DELETE",
    )


RecommendedContactFormset = formset_factory(RecommendedContactForm, can_delete=True)

RecommendedContactInlineFormset = inlineformset_factory(
    ReferentContact,
    RecommendedContact,
    form=RecommendedContactForm,
    fields=[
        "first_name",
        "last_name",
        "website",
        "structure",
        "function",
        "engagements",
        "reasons_to_contact",
        "fields_of_competence",
        "other_fields_of_competence",
    ],
    extra=1,
    can_delete=True,
)
