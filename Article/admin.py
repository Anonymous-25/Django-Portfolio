from django.contrib import admin
from .models import *
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "is_published",
        "is_featured",
        "views",
        "likes",
        "created_at",
    )
    list_filter = (
        "is_published",
        "is_featured",
        "category",
        "tags",
        "created_at",
    )
    search_fields = (
        "title",
        "excerpt",
        "content",
    )
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    readonly_fields = ("views","likes", "created_at", "updated_at")
    date_hierarchy = "created_at"