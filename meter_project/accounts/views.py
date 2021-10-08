from rest_framework import serializers
from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

from .models import Customer
from .serializers import RegistrationSerializer, CustomerSerializer


@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# class LogoutView(generics.CreateAPIView):

#     def logout_view(request):
#         if request.method == 'POST':
#             request.user.auth_token.delete()
#             return Response(status=status.HTTP_200_OK)



@api_view(['POST'])
def registration_view(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name

            refresh = RefreshToken.for_user(account)
            # token = Token.objects.get(user=account).key
            
            data['token'] = {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                            }

        else:
            data = serializer.errors

        return Response(data)


class SearchUserView(generics.ListAPIView):
    
    queryset = Customer.objects.all()
    serializer_class = RegistrationSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['username', 'email']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']


class CustomerDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def patch(self, request, *args, **kwargs):   
        if request.query_params.get('owner') is not None:
            owner = Customer.objects.get(username=request.query_params.get('owner'))
            model = apps.get_model(app_label='core', model_name='meter')

            content_type = ContentType.objects.get_for_model(model)
            all_permissions = Permission.objects.filter(content_type=content_type)

            # print (all_permissions)
            for i in all_permissions:
                owner.user_permissions.add(i)
            return HttpResponse('Success')

        return super().patch(request, *args, **kwargs)  