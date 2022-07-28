from django.contrib.auth.models import User
from rest_framework import serializers
from user_app.models import CustomUser
# Create your models here.


class LoginSerializer(serializers.Serializer):

    class Meta:
        model = CustomUser
        fields = ['username','password']

    

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username','email','password','password2']
        extra_kwargs={
            'password' : {'write_only' : True}  
        }
    
    def save(self):
        password  = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': ' Passwords should match'})

        if CustomUser.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error' : 'Email already exists'})

        if CustomUser.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error' : 'username already taken'})

        account = CustomUser(email=self.validated_data['email'],username = self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account
        
        
