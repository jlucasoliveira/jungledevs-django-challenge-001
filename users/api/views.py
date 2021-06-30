from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from django.contrib.auth import authenticate, get_user_model, logout
from django.utils.translation import gettext_lazy

from . import serializers as api_serializers

User = get_user_model()


class AuthViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == "login":
            return api_serializers.LoginSerializer
        elif self.action == "sign_up":
            return api_serializers.RegisterSerializer
        return super().get_serializer_class()

    @action(methods=["POST"], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, **serializer.data)
        if not user:
            raise NotFound(gettext_lazy("As credenciais fornecidas estão incorretas."))
        user.auth_token, _ = Token.objects.get_or_create(user=user)
        response_data = api_serializers.AuthenticatedUserSerializer(user)
        return Response(status=status.HTTP_200_OK, data=response_data.data)

    @action(methods=["POST"], detail=False, permission_classes=[IsAuthenticated])
    def logout(self, request):
        Token.objects.filter(user=request.user).delete()
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["POST"], detail=False, url_path="sign-up")
    def sign_up(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.data)
        user.auth_token, _ = Token.objects.get_or_create(user=user)
        response_serializer = api_serializers.AuthenticatedUserSerializer(user)
        return Response(status=status.HTTP_201_CREATED, data=response_serializer.data)
