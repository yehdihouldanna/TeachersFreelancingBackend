
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user_app.api.serializers import RegistrationSerializer,LoginSerializer
# from rest_framework.authtoken.models import Token
# from user_app import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



@api_view(['POST'])
def login_view(request):
    if request.method=='POST':
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        user = authenticate(username=request.data['username'], password=request.data['password']) # check for email and password
        if not user : #or user.phone_number !=data['phone_number']: #check for phone number
            raise serializer.ValidationError({"detail":"Incorrect email,phone or password"})
        response = get_tokens_for_user(user)
        return Response(response,status=status.HTTP_200_OK)

@api_view(['POST',])
def log_out_view(request):
    if request.method=='POST':
        request.user.auth_token.delete()
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

            # token = Token.objects.get(user=account).key
            # data['token'] = token

            #?using jwt token
            data['token'] = get_tokens_for_user(user=account)


        else :
            data = serializer.errors 

        return Response(data,status=status.HTTP_201_CREATED)

