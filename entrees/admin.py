from django.contrib import admin

from .models import FieldOfCompetence, RecommendedContact, ReferentContact

admin.site.register(FieldOfCompetence)
admin.site.register(ReferentContact)
admin.site.register(RecommendedContact)
