from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import permissions, generics, status
from rest_framework.views import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import TokenSerializer


class GetUserToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # authentication_classes = (BasicAuthentication)
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'email': user.email,
            'username': user.username,
        })


class DeleteUserToken(generics.DestroyAPIView):
    queryset = Token.objects.all()
    permissions_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(key=request.auth)
            token.delete()
            return Response({"detail": "Token Deleted Successfully"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"detail": "Token Not Provided"}, status=status.HTTP_401_UNAUTHORIZED)