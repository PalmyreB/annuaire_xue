from django.contrib import admin

from .models import FieldOfCompetence, ReferentContact, RecommendedContact

admin.site.register(FieldOfCompetence)
admin.site.register(ReferentContact)
admin.site.register(RecommendedContact)
