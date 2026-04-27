from django.contrib import admin
from .models import *
# ========[ Portfolio Category Admin ]=======
@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
# ========[ Portfolio Item Admin ]=======
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "featured")
    list_filter = ("categories", "featured")
    search_fields = ("title", "description")
# ========[ Work Admin ]=======
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    