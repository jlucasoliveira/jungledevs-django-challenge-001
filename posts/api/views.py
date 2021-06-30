from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny

from posts import models
from posts.api import serializers as api_serializers


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects
    serializer_class = api_serializers.AuthorSerializer
    parser_classes = [MultiPartParser]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects
    serializer_class = api_serializers.CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.prefetch_related("category", "author")
    serializer_class = api_serializers.ArticleSerializer


class ArticleReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Article.objects.prefetch_related("category", "author")
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == "retrieve":
            if self.request.user.is_anonymous:
                return api_serializers.ArticleSerializerPublic
            return api_serializers.ArticleSerializerPrivate
        elif self.action == "list":
            return api_serializers.ArticleSerializerList

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get("category", None)
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset
