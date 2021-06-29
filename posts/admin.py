from django.contrib import admin

from posts import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("nane",)
