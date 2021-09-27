from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['name', 'surname', 'username','email', 'password', 'password2', 'description']
        extra_kwargs = {
            'password':{'write_only':True}
            }

    def save(self):

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error':'Both passwords should be the same!'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists!'})

        account = User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account
   