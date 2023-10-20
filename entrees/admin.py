from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from entrees.models import FieldOfCompetence, RecommendedContact, ReferentContact


class ReferenctContactInline(admin.StackedInline):
    model = ReferentContact
    can_delete = False


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ReferenctContactInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class RecommendedContactAdmin(admin.ModelAdmin):
    list_filter = ["fields_of_competence"]


admin.site.register(FieldOfCompetence)
admin.site.register(ReferentContact)
admin.site.register(RecommendedContact, RecommendedContactAdmin)
