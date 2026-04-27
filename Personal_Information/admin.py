from django.contrib import admin
from .models import *
# ===============[ Profile Admin] ===============
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Basic Info", {
            "fields": (
                "name",
                "designation",
                "email",
                "status",
                "location",
                "profile_picture",
            )
        }),
        ("Links", {
            "fields": (
                "github",
                "linkedin",
                "discord",
                "reddit",
                "dev",
            )
        }),
        ("Description", {
            "fields": (
                "about",
                "location_url",
            )
        }),
    )
    list_display = ("name", "designation", "email", "status")
    def has_add_permission(self, request):
        if Profile.objects.exists():
            return False
        return True
# ===============[ Education Admin] ===============
from django.contrib import admin
from .models import Education
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("name", "institution", "duration", "score")
    search_fields = ("name", "institution")
# ===============[ Certification Admin] ===============
@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("certificate_name", "provider_name")
    search_fields = ("certificate_name", "provider_name")
# ===============[ Experience Admin] ===============
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("designation", "organization", "duration")
    search_fields = ("designation", "organization")
# ===============[ Skill Admin] ===============
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("skill_name", "percentage")