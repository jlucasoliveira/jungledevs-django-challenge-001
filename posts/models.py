from os import path
from uuid import uuid4

from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class IdModelMixin(models.Model):
    # Apesar que no exemplo ser uuid3 não foi informado o namespace e name para geração da id
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
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


class Category(IdModelMixin):
    name = models.CharField(verbose_name=_("nome"), max_length=150)
    slug = models.SlugField(verbose_name=_("identificador"), unique=True, db_index=True)

    class Meta:
        verbose_name = _("categoria")
        ordering = ["slug"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._actual_slug = self.name

    def save(self, *args, **kwargs) -> None:
        if not self.slug or self._actual_slug != self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Article(IdModelMixin):
    title = models.CharField(verbose_name=_("titulo"), max_length=150)
    summary = models.CharField(verbose_name=_("sumário"), max_length=200)
    author = models.ForeignKey(
        to="posts.Author",
        on_delete=models.deletion.CASCADE,
        verbose_name=_("autor"),
    )
    category = models.ForeignKey(to="posts.Category", on_delete=models.deletion.CASCADE, verbose_name=_("categoria"))
    first_paragraph = models.TextField(
        verbose_name=_("primeiro paragrafo"),
        max_length=450,
    )
    body = models.TextField(verbose_name=_("conteúdo"))
    created_at = models.DateTimeField(verbose_name=_("data de criação"), default=now)

    class Meta:
        verbose_name = _("artigo")
        ordering = ["-created_at"]
