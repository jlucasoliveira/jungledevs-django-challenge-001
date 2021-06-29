from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser

from posts import models
from posts.api import serializers as api_serializers


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects
    serializer_class = api_serializers.AuthorSerializer
    parser_classes = [MultiPartParser]
