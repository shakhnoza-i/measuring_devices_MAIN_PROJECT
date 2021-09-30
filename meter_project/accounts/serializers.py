from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


for user in User.objects.all():
    Token.objects.get_or_create(user=user)


class RegistrationSerializer(serializers.ModelSerializer):


    name = serializers.CharField(max_length = 30)
    surname = serializers.CharField(max_length = 30)
    password2 = serializers.CharField(style = {'input_type':'password'}, write_only=True)
    description = serializers.CharField(max_length = 255)

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

        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error':'Username already exists!'})

        account = User(email=self.validated_data['email'],username=self.validated_data['username'], 
        name=self.validated_data['name'], surname=self.validated_data['surname'])
        account.set_password(password)
        account.save()

        return account
   