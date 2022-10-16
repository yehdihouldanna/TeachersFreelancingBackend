# from django.contrib.auth.models import User
from wsgiref import validate
from rest_framework import serializers
from user_app.models import  User , Teacher , Student,Account,Transaction
from backend.utils.utils import *
from django.core.files.base import ContentFile, File
from django.db import transaction
# Create your models here.

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
import os
from teacher_freelance import settings
from backend.models_basic import Subject,Classe,Specialty,Disponibility
from backend.api.serializers_basic import DisponibilitySerializer, SubjectSerializer,ClasseSerializer,SpecialtySerializer

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
    
    #TODO Create an account on user creation
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

        user = User(phone=self.validated_data['phone'],email=self.validated_data['email'],username = self.validated_data['username'])
        user.set_password(password)
        user.save()

        return user
        
#? when working with serializers you can forget about the *forms* , the serializers offers more flexible ways to receive and form data.
class TeacherRegistrationSerializer(serializers.ModelSerializer):
    # user = RegistrationSerializer()
    phone = serializers.IntegerField(required=False)
    username = serializers.CharField(required=False,max_length=150)
    email = serializers.EmailField(required=False,max_length=150)
    
    password = serializers.CharField(style={'input_type':'password'},write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    disponibilities = DisponibilitySerializer(many=True,read_only=True)
    classes = ClasseSerializer(many=True,read_only=True) 
    subjects=  SubjectSerializer(many=True,read_only=True) 
    class Meta:
        model = Teacher
        fields = ['username','email','phone','password','password2','diploma','introduction',
        'hourly_wage','subjects','disponibilities','classes']
        extra_kwargs={
            'password' : {'write_only' : True},
        }
    
    def phone_validator(self,phone):
        print(f"checked the type of the phone number and it's {type(phone)}")

    @transaction.atomic
    def create(self,validated_data):
        try :
            with transaction.atomic():
                user_data = {}
                user_data['username'] = validated_data.pop('username')
                user_data['phone'] = validated_data.pop('phone')
                user_data['email'] = validated_data.pop('email')
                user_data['password'] = validated_data.pop('password')
                user_data['password2'] = validated_data.pop('password2')
                user_data['is_teacher'] = True
                registration_ser = RegistrationSerializer(data=user_data)
                if registration_ser.is_valid():
                    user = registration_ser.save()
                    user.is_teacher =True
                    user.save()
                    account = Account.objects.create(user=user)
                    account.save()
                    # validated_data["disponibilities"] = format_disponitbilites(validated_data.pop("disponibilities"))
                    
                    if self.initial_data['diploma']:
                        extension = self.initial_data['diploma'].name.split(".")[-1]
                        name="diploma_"+user_data['username']+"."+extension
                        diploma = File(self.initial_data['diploma'], name=name)
                    else :
                        diploma= None
                    try:
                        validated_data.pop("diploma")
                    except :
                        pass
                    
                    # subjects = validated_data.pop("subjects")
                    # disponibilities = validated_data.pop("diponibilities")
                    # classes = validated_data.pop("classes")
                    # specialties = validated_data.pop("specialties")

                    teacher = Teacher.objects.create(user=user,diploma=diploma,**validated_data)
                    
                    
                    if 'subjects' in self.initial_data.keys():
                        if type(self.initial_data['subjects'])== str:
                            self.initial_data['subjects']= self.initial_data['subjects'].split(",")
                        for suj in self.initial_data['subjects'] :
                            try :
                                sujet = Subject.objects.get(pk=suj)
                                teacher.subjects.add(sujet)
                            except :
                                raise serializers.ValidationError({'error': f' Subject "{suj}" does not exist'})

                    if 'classes' in self.initial_data.keys():  
                        if type(self.initial_data['classes'])== str:
                            self.initial_data['classes']= self.initial_data['classes'].split(",")
                    
                        for cl in self.initial_data['classes'] :
                            try :
                                cl_ = Classe.objects.get(name=cl)
                                teacher.classes.add(cl_)
                            except :
                                raise serializers.ValidationError({'error': f' Classe "{cl}" does not exist'})
                    if 'disponibilities' in self.initial_data.keys():
                        if type(self.initial_data['disponibilities'])== str:  
                            self.initial_data['disponibilities']= self.initial_data['disponibilities'].split(",") 
                        for day in self.initial_data['disponibilities'] :
                            try :
                                day = Disponibility.objects.get(name=day.title())
                                teacher.disponibilities.add(day)
                            except :
                                raise serializers.ValidationError({'error': f' Day "{day}" does not exist'})

                    if 'specialties' in self.initial_data.keys():
                        if type(self.initial_data['specialties'])== str:
                            self.initial_data['specialties']= self.initial_data['specialties'].split(",") 
                        for speci in self.initial_data['specialties'] :
                            try :
                                sp = Specialty.objects.get(name=speci)
                                teacher.specialties.add(sp)
                            except :
                                raise serializers.ValidationError({'error': f' Specialty "{sp}" does not exist'})
                    teacher.save()

                    return teacher
                raise  serializers.ValidationError(registration_ser.errors)
        except  serializers.ValidationError as error:
            raise serializers.ValidationError(error.args)


class StudentRegistrationSerializer(RegistrationSerializer):
    
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
        user = super().save()
        user.is_student=True
        user.save()

        try:
            classe = self.validated_data['classe']
        except:
            classe = None
        try:
            speciality = self.validated_data['speciality']
        except :
            speciality = None
        student = Student(
            user = user,classe=classe,speciality=speciality)
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
    user_student = UserSerializer()
    classe = ClasseSerializer()
    specilaty = SpecialtySerializer()
    class Meta:
        model = Student
        fields = '__all__'
    

class AccountSerializer(serializers.ModelSerializer):
    # transactions = TransactionSerializer(many=True, read_only = True)
    user = UserSerializer()
    class Meta : 
        model = Account
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="account.user__username")
    # account = AccountSerializer()
    class Meta:
        model = Transaction
        fields = '__all__'
