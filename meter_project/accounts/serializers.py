from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Customer


for user in Customer.objects.all():
    Token.objects.get_or_create(user=user)


class RegistrationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Customer
        fields = "__all__"
        
        extra_kwargs = {
            'password':{'write_only':True}
            }

    def save(self):

        password = self.validated_data['password']
    
        if Customer.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists!'})

        if Customer.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error':'Username already exists!'})

        account = Customer(email=self.validated_data['email'],username=self.validated_data['username'], 
        first_name=self.validated_data['first_name'], last_name=self.validated_data['last_name'])
        account.set_password(password)
        account.save()

        return account
