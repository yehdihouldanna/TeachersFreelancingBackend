# from django.contrib.auth.models import User
from rest_framework import serializers
from user_app.models import User , Teacher , Student
from backend.utils.utils import *
# Create your models here.


class LoginSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ['username','password']

    

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs={
            'password' : {'write_only' : True}  
        }
    
    def save(self):
        password  = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': ' Passwords should match'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error' : 'Email already exists'})

        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error' : 'username already taken'})

        account = User(email=self.validated_data['email'],username = self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account
        
        
from rest_framework import serializers

#? when working with serializers you can forget about the *forms* , the serializers offers more flexible ways to receive and form data.
class TeacherRegistrationSerializer(serializers.ModelSerializer):
    
    phone = serializers.IntegerField(required=True)
    username = serializers.CharField(required=True,max_length=150)
    email = serializers.EmailField(required=True,max_length=150)
    
    password = serializers.CharField(style={'input_type':'password'},write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Teacher
        fields = ['username','email','phone','password','password2','diploma','introduction',
        'hourly_wage','subjects','disponibilities']
        extra_kwargs={
            'password' : {'write_only' : True}  
        }
    
    def phone_validator(self,phone):
        print(f"checked the type of the phone number and it's {type(phone)}")

    def save(self):
        password  = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': ' Passwords should match'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error' : 'Email already exists'})

        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error' : 'username already taken'})

        if User.objects.filter(phone=self.validated_data['phone'].exists()):
            raise serializers.ValidationError({'error' : 'phone number already_exist'})

        self.phone_validator(self.validated_data['phone'])
        account = User(email=self.validated_data['email'],username = self.validated_data['username'],phone=self.validated_data['phone'])
        account.set_password(password)
        account.save()

        teacher = Teacher(
            user = account,diploma=self.validated_data['diploma'],
            introduction=self.validated_data['introduction'],
            hourly_wage=self.validated_data['hourly_wage'],
            subjects=self.validated_data['subjects'],
            disponibilities=self.validated_data['disponibilities'])

        teacher.save()
        return teacher