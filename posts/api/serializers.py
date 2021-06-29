from rest_framework import serializers

from posts import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ("id", "name", "picture")
