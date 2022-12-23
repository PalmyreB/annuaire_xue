from django.utils.translation import gettext as _


class ReferentContactForm(ModelForm):
    prefix = "referent"

    class Meta:
        model = ReferentContact
        fields = ["lastname", "firstname", "mail", "phone", "city", "promotion"]

    layout = Layout(
        Row("firstname", "lastname"), "mail", Row("phone", "city", "promotion")
    )


class RecommendedContactForm(ModelForm):
    prefix = "recommended"
    has_approved = BooleanField(
        label=_(
            "Je confirme que je m'engage à servir d'intermédiaire pour mettre en relation des personnes d'X-UE avec ce contact."
        )
    )
    has_informed = BooleanField(
        label=_(
            "Je confirme que mon contact secondaire est informé qu'il figurera dans cet annuaire. "
        )
    )

    class Meta:
        model = RecommendedContact
        fields = [
            "firstname",
            "lastname",
            "website",
            "structure",
            "function",
            "engagements",
            "reasons_to_contact",
            "fields",
            "other_fields",
        ]

    # layout = Layout(
    #     Row("firstname", "lastname"),
    #     "website",
    #     Row("structure", "function"),
    #     "engagements",
    #     "reasons_to_contact",
    #     "fields",
    #     "other_fields",
    # )


RecommendedContactFormset = formset_factory(RecommendedContactForm, can_delete=True)
