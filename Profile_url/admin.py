from django.utils.html import format_html
from .models import Profile_url
from django.contrib import admin
@admin.register(Profile_url)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile_url', 'image_preview')
    def image_preview(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="50" height="50" />', obj.image_url)
        return "No Image"
    image_preview.short_description = "Image"