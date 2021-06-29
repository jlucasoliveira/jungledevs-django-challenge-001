from django.contrib import admin

from posts import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("nane",)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "summary", "category")
    search_fields = ("title", "author")
    readonly_fields = ("created_at",)
