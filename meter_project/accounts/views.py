from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from accounts.serializers import RegistrationSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth.models import User


class LogoutView(generics.CreateAPIView):

    def logout_view(request):
        if request.method == 'POST':
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)


class RegistrationView(generics.CreateAPIView):

    def registration_view(request):
        if request.method == 'POST':
            serializer = RegistrationSerializer(data = request.data)
            data = {}


            if serializer.is_valid():
                account = serializer.save()
                data['response'] = "Registration Successful!"
                data['username'] = account.username
                data['email'] = account.email

                # token = Token.objects.get(user=account).key
                # data['token'] = token
                refresh = RefreshToken.for_user(account)
                data['token'] = {
                                    'refresh': str(refresh),
                                    'access': str(refresh.access_token),
                                }

            else:
                data = serializer.errors

            return Response(data)


class SearchUserView(generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']