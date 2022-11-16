from django.db import models


class Field(models.Model):
    name = models.CharField("Nom", max_length=200)
    slug = models.SlugField("Code", null=False, unique=True)

    def __str__(self):
        return self.name


class ReferentContact(models.Model):
    lastname = models.CharField("Nom", max_length=200)
    firstname = models.CharField("Prénom", max_length=200)
    mail = models.EmailField("Adresse email", max_length=200)
    phone = models.CharField(
        "Numéro de téléphone",
        max_length=200,
        blank=True,
        help_text="Au format +33 6 00 00 00 00",
    )
    city = models.CharField("Ville", max_length=200, blank=True)
    promotion = models.CharField(
        "Promotion",
        max_length=200,
        blank=True,
        help_text="Au format X04 pour le cycle ingénieur polytechnicien, D98 pour le doctorat de Polytechnique, M09 pour le master, B22 pour le bachelor",
    )
    registration_date = models.DateTimeField("Date d'inscription")

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)


class RecommendedContact(models.Model):
    lastname = models.CharField("Nom", max_length=200)
    firstname = models.CharField("Prénom", max_length=200)
    website = models.URLField("Site personnel", max_length=200, blank=True)
    structure = models.CharField("Structure", max_length=200, blank=True)
    function = models.CharField("Fonction", max_length=200, blank=True)
    engagements = models.TextField("Engagements")
    reasons_to_contact = models.TextField(
        "Raisons pour lesquelles on peut contacter cette personne", blank=True
    )
    fields = models.ManyToManyField(
        Field, verbose_name="Domaines de compétence", blank=True
    )
    other_fields = models.CharField(
        "Autres domaines de compétence",
        max_length=500,
        blank=True,
        help_text="Sépare les domaines par des virgules, par exemple : Bilan carbone, Communication",
    )
    referent_contact = models.ForeignKey(ReferentContact, verbose_name="Contact référent", on_delete=models.PROTECT)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)
