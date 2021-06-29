from rest_framework import serializers

from posts import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ("id", "name", "picture")


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.Category
        fields = (
            "id",
            "name",
            "slug",
        )
