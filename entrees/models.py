from django.db import models
from django.utils.translation import gettext as _


    name = models.CharField(_("nom"), max_length=200)
    slug = models.SlugField(_("code"), null=False, unique=True)

    class Meta:
        verbose_name = _("domaine de compétence")
        verbose_name_plural = _("domaines de compétence")

    def __str__(self):
        return self.name


class ReferentContact(models.Model):
    first_name = models.CharField(_("prénom"), max_length=200)
    last_name = models.CharField(_("nom de famille"), max_length=200)
    mail = models.EmailField(_("adresse email"), max_length=200)
    phone = models.CharField(
        _("numéro de téléphone"),
        max_length=200,
        blank=True,
        help_text=_("Au format +33 6 00 00 00 00"),
    )
    city = models.CharField(_("ville"), max_length=200, blank=True)
    promotion = models.CharField(
        _("promotion"),
        max_length=200,
        blank=True,
        help_text=_(
            "Au format X04 pour le cycle ingénieur polytechnicien, D98 pour le doctorat de Polytechnique, M09 pour le master, B22 pour le bachelor"
        ),
    )
    registration_date = models.DateTimeField(_("date d'inscription"))

    class Meta:
        verbose_name = _("contact référent")
        verbose_name_plural = _("contacts référents")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class RecommendedContact(models.Model):
    first_name = models.CharField(_("prénom"), max_length=200)
    last_name = models.CharField(_("nom de famille"), max_length=200)
    website = models.URLField(_("site personnel"), max_length=200, blank=True)
    structure = models.CharField(_("structure"), max_length=200, blank=True)
    function = models.CharField(_("fonction"), max_length=200, blank=True)
    engagements = models.TextField(_("engagements"))
    reasons_to_contact = models.TextField(
        _("raisons pour lesquelles on peut contacter cette personne"), blank=True
    )
    fields = models.ManyToManyField(
        Field, verbose_name=_("domaines de compétence"), blank=True
    )
    other_fields = models.CharField(
        _("autres domaines de compétence"),
        max_length=500,
        blank=True,
        help_text=_(
            "Sépare les domaines par des virgules, par exemple : Bilan carbone, Communication"
        ),
    )
    referent_contact = models.ForeignKey(
        ReferentContact, verbose_name=_("contact référent"), on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _("contact recommandé")
        verbose_name_plural = _("contacts recommandés")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
