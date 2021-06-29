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


class ArticleSerializerMixin(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = models.Article
        fields = ("id", "author", "category", "title", "summary")


class ArticleSerializerList(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = models.Article
        fields = ("id", "author", "category", "title", "summary")


class ArticleSerializerPublic(ArticleSerializerList):
    firstParagraph = serializers.CharField(source="first_paragraph")

    class Meta:
        model = models.Article
        fields = ("id", "author", "category", "title", "summary", "firstParagraph")


class ArticleSerializer(ArticleSerializerPublic):
    class Meta:
        model = models.Article
        fields = ("id", "author", "category", "title", "summary", "firstParagraph", "body")
