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
        fields = ("id", "name", "slug")


class ArticleSerializer(serializers.ModelSerializer):
    firstParagraph = serializers.CharField(source="first_paragraph")

    class Meta:
        model = models.Article
        fields = (
            "id",
            "author",
            "category",
            "title",
            "summary",
            "firstParagraph",
            "body",
        )


class ArticleSerializerList(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = serializers.StringRelatedField()

    class Meta:
        model = models.Article
        fields = ("id", "author", "category", "title", "summary")


class ArticleSerializerPublic(ArticleSerializer, ArticleSerializerList):
    class Meta:
        model = models.Article
        fields = ("id", "author", "category", "title", "summary", "firstParagraph")


class ArticleSerializerPrivate(ArticleSerializer, ArticleSerializerList):
    class Meta:
        model = models.Article
        fields = (
            "id",
            "author",
            "category",
            "title",
            "summary",
            "firstParagraph",
            "body",
        )
