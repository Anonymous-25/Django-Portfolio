from django.contrib import admin
from .models import *
# ===============[ WebSettings Admin] ===============
@admin.register(WebSettings)
class WebSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if WebSettings.objects.exists():
            return False
        return True
# ===============[ SEOSettings Admin] ===============
@admin.register(SEOSettings)
class SEOSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if SEOSettings.objects.exists():
            return False
        return True
admin.site.site_header = "Castle"
admin.site.site_title = "Portfolio Dashboard"
admin.site.index_title = "Welcome to Admin"