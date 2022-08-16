# from django.contrib.auth.models import User
from rest_framework import serializers
from user_app.models import User , Teacher , Student, format_disponitbilites
from backend.utils.utils import *
# Create your models here.

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class UserLoginSerializer(serializers.Serializer):

    # email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        # email = data.get("email", None)
        # username = data.get("username", None)
        password = data.get("password", None)
        username = data.get("username",None) # this username can contain the phone number to authenticate with
        
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this phone and password is not found.'
            )
        try:
            refresh = RefreshToken.for_user(user)

            data = {    'id' : user.id,
                        'is_teacher' : user.is_teacher,
                        'is_student' : user.is_student,
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given phone and password does not exists'
            )
        return data


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['phone','username','password']

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['phone','username','email','password','password2']
        extra_kwargs={
            'password' : {'write_only' : True},
            # 'username' : {'required' , False},
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

        if User.objects.filter(phone=self.validated_data['phone']).exists():
            raise serializers.ValidationError({'error' : 'phone already taken'})

        account = User(phone=self.validated_data['phone'],email=self.validated_data['email'],username = self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account
        
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
            'password' : {'write_only' : True},
            # 'username' : {'required' , False}
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

        if User.objects.filter(phone=self.validated_data['phone']).exists():
            raise serializers.ValidationError({'error' : 'phone number already_exist'})

        self.phone_validator(self.validated_data['phone'])
        account = User(is_teacher=True,email=self.validated_data['email'],username = self.validated_data['username'],phone=self.validated_data['phone'])
        account.set_password(password)
        account.save()


        # formating disponibilities : 
        
        disponibilities = format_disponitbilites(self.validated_data['disponibilities'])

        teacher = Teacher(
            user = account,diploma=self.validated_data['diploma'],
            introduction=self.validated_data['introduction'],
            hourly_wage=self.validated_data['hourly_wage'],
            subjects=self.validated_data['subjects'],
            disponibilities=disponibilities)

        teacher.save()
        return teacher
class StudentRegistrationSerializer(serializers.ModelSerializer):
    
    phone = serializers.IntegerField(required=True)
    username = serializers.CharField(required=True,max_length=150)
    email = serializers.EmailField(required=True,max_length=150)
    
    password = serializers.CharField(style={'input_type':'password'},write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Student
        fields = ['username','email','phone','password','password2','classe','speciality']
        extra_kwargs={
            'password' : {'write_only' : True},
            # 'username' : {'required' , False}

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

        if User.objects.filter(phone=self.validated_data['phone']).exists():
            raise serializers.ValidationError({'error' : 'phone number already_exist'})

        self.phone_validator(self.validated_data['phone'])
        account = User(is_student=True,email=self.validated_data['email'],username = self.validated_data['username'],phone=self.validated_data['phone'])
        account.set_password(password)
        account.save()

        student = Student(
            user = account,classe=self.validated_data['classe'],
            speciality=self.validated_data['speciality'])

        student.save()
        return student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","last_login","username","first_name","last_name","email","date_joined","phone"]

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Teacher
        fields = '__all__'
        extra_kwargs = {"user" : {'required' : False}}


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = '__all__'
    