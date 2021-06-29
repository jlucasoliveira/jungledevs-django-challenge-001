from os import path
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class IdModelMixin(models.Model):
    # Apesar que no exemplo ser uuid3 não foi informado o namespace e name para geração da id
    id = models.UUIDField(
        primary_key=True,
        default=uuid4(),
        unique=True,
        editable=False,
    )

    class Meta:
        abstract = True


def profile_path(instance, filename) -> str:
    ext = filename.split(".")[-1]
    return path.join("author", "picture", f"{uuid4()}.{ext}")


class Author(IdModelMixin):
    name = models.CharField(verbose_name=_("nome"), max_length=200)
    picture = models.ImageField(
        verbose_name=_("foto de perfil"),
        upload_to=profile_path,
        blank=True,
    )

    class Meta:
        verbose_name = _("autor")
        verbose_name_plural = _("autores")
        ordering = ["name"]

    def __str__(self):
        return self.name
