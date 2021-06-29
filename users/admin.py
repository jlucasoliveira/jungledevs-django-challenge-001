from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    list_display = ("name", "email", "is_staff")
    search_fields = ("name",)
    ordering = ("email",)
    readonly_fields = ("date_joined",)
    add_fieldsets = ((None, {"fields": ("name", "email", "password1", "password2")}),)
    fieldsets = (
        (_("Personal info"), {"fields": ("name", "email", "password")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "user_permissions", "groups")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
