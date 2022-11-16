from django.contrib import admin

from .models import Field, ReferentContact, RecommendedContact

admin.site.register(Field)
admin.site.register(ReferentContact)
admin.site.register(RecommendedContact)
