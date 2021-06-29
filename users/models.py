from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import managers


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, db_index=True)
    name = models.CharField(verbose_name=_("nome"), max_length=200)
    is_staff = models.BooleanField(
        verbose_name=_("membro da equipe"),
        default=False,
        help_text=_("Permite que este usuário tenha acesso ao painel admin."),
    )
    is_active = models.BooleanField(verbose_name=_("ativo"), default=True)
    date_joined = models.DateTimeField(
        verbose_name=_("data de admissão"),
        auto_now_add=True,
    )

    objects = managers.UserManager()

    REQUIRED_FIELDS = ["name"]
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("usuário")
        ordering = ["email"]
