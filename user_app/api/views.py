
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from user_app.api.serializers import TeacherSerializer,StudentSerializer, RegistrationSerializer,UserLoginSerializer,LoginSerializer,TeacherRegistrationSerializer,StudentRegistrationSerializer
from user_app.models import Teacher,Student
from user_app.api.permissions import IsTheCurrentUser
# from rest_framework.authtoken.models import Token
# from user_app import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
import json

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def login_view(request):
    if request.method=='POST':
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        return Response(data,status=status.HTTP_200_OK)
        
        
        # if serializer.is_valid():
        #     account = serializer.save()

        #     data['response'] = "Registration Successful!"
        #     data['username'] = account.username
        #     data['email'] = account.email

        # user = authenticate(username=request.data['username'], password=request.data['password']) # check for email and password
        # if not user : #or user.phone_number !=data['phone_number']: #check for phone number
        #     raise serializers.ValidationError({"detail":"Incorrect email, phone or password"})
        # response = get_tokens_for_user(user)
        # return Response(response,status=status.HTTP_200_OK)



@api_view(['POST',])
def log_out_view(request):
    if request.method=='POST':
        try :
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        except : #? the jwt token will stay valid for it's whole duration, to logout the client has to delete its access token from the cache.
            print("Error : Custom Front 0x0001") # u need to delete the jwt acess token from the fronend
            return Response(status=status.HTTP_200_OK)


@api_view(['POST',])
def registration_view(request):
    if request.method=='POST':
        serializer = RegistrationSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email
            data['phone'] = account.phone

            # token = Token.objects.get(user=account).key
            # data['token'] = token

            #? using jwt token
            data['token'] = get_tokens_for_user(user=account)


        else :
            data = serializer.errors 

        return Response(data,status=status.HTTP_201_CREATED)

@api_view(['POST'])
def register_teacher_view(request):
    # We have a json fields in our data so we need to process the data
    # before passing it to the serializer
    try:
        input_data = json.loads(request.body)
    except:
        return Response({"message": "ERROR DETECT"})
        #      use data, not request.data ↓
    print(input_data)
    serializer = TeacherRegistrationSerializer(data=input_data)
    
    data = {}
    if serializer.is_valid():
        teacher_data = serializer.save()
        data['response'] = "Teacher registration successful!"
        data['username'] = teacher_data.user.username
        data['email']=teacher_data.user.email
        data['phone']=teacher_data.user.phone
        data['is_teacher']=teacher_data.user.is_teacher
        data['introduction'] =teacher_data.introduction
        data['hourly_wage'] = teacher_data.hourly_wage
        data['diploma']=teacher_data.diploma.__repr__()
        data['token'] = get_tokens_for_user(user=teacher_data.user)

    else :
        data = serializer.errors 

    return Response(data,status=status.HTTP_201_CREATED)

@api_view(['POST'])
def register_student_view(request):
   
    serializer = StudentRegistrationSerializer(data=request.data)
    
    data = {}
    if serializer.is_valid():
        student_data = serializer.save()
        data['response'] = "Student registration successful!"
        data['id']= student_data.user.pk
        data['username'] = student_data.user.username
        data['email']=student_data.user.email
        data['phone']=student_data.user.phone
        data['is_student']=student_data.user.is_student
        data['classe'] =student_data.classe
        data['speciality'] = student_data.speciality
        data['token'] = get_tokens_for_user(user=student_data.user)

    else :
        data = serializer.errors 

    return Response(data,status=status.HTTP_201_CREATED)


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsTheCurrentUser]
    serializer_class = TeacherSerializer

    def get_queryset(self):
        user = self.request.user
        return Teacher.objects.filter(user=user)

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsTheCurrentUser]
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(user=user)

class TeacherListView(generics.ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    queryset = Teacher.objects.all()
    #TODO create custom filters for the teachers based , subjects , and diponibilities