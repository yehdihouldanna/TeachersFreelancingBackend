from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from backend.utils.utils import *
from user_app.api.views import get_tokens_for_user
#?when using the Class TestCase which is the base for all tests in django, it will create a new database in which it does the tests without affecting our actual database

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        data = {
            "username" : "testcase",
            "email" : "testcase@testcase.testcase",
            "password":"NewPassword.123",
            "password2":"NewPassword.123"
        }
        response = self.client.post(reverse('register'),data)
        # dprint(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        tprint_OK()

    def setUp(self):
        """this help create a user to test the functionalities that require an existing user"""
        self.user = User.objects.create_user(username="Red",password="Color.123")

    

    def test_login(self):
        data = {
            "username":"Red",
            "password":"Color.123"
            }
        response = self.client.post(reverse('login'),data)
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        tprint_OK()
        

    def test_logout(self):

        #? Nomal auth token
        # self.token = Token.objects.get(user__username="example")
        # self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

        #? simple_jwt token
        self.token = get_tokens_for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token['access'])

        # dprint(self.token)

        response = self.client.post(reverse('logout'))

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        tprint_OK()
        