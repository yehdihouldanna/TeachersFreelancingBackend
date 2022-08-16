from user_app.models import Teacher,Student, User
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
            "phone" : "+22210000000",
            "username" : "testcase",
            "email" : "testcase@testcase.testcase",
            "password":"NewPassword.123",
            "password2":"NewPassword.123"
        }
        response = self.client.post(reverse('register'),data)
        # dprint(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        tprint_OK()

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        data = {
            "phone" : "+22210000000",
            "username" : "testcase",
            "email" : "testcase@testcase.testcase",
            "password":"NewPassword.123",
            "password2":"NewPassword.123"
        }
        response = self.client.post(reverse('register'),data)
        # dprint(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        tprint_OK()

    def test_create_teacher(self):
        """
        Ensure we can create a new teacher object.
        """
        data = {
            "username" : "teacher_instance_test",
            "email" : "teacher_instance_test@example.com",
            "phone":"+22210000005",
            "password" : "Color.123",
            "password2" : "Color.123",
            "subjects":["Mathématiques","Physique Chimie"],
            "introduction" : "The first teacher registered on the test database.",
            "diploma":None,
            "hourly_wage":"200",
            "disponibilities" :{"lundi":["8","9","16","17","18"],"mardi":["20","21"]
            }
        }

        response = self.client.post(reverse('register_teacher'),data,format="json")
        # dprint(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        tprint_OK()
    def test_create_student(self):
        """
        Ensure we can create a new student object.
        """
        data = {
            "username" : "student_instance_test",
            "email" : "student_instance_test@example.com",
            "phone":"+22210000005",
            "password" : "Color.123",
            "password2" : "Color.123",
            "classe":"99",
            "speciality" : ""
            }

        response = self.client.post(reverse('register_student'),data)
        # dprint(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        tprint_OK()

    def setUp(self):
        """this help create a user to test the functionalities that require an existing user"""
        self.user = User.objects.create_user(phone="+22210000001",username="Red",password="Color.123")
        user_t_data = {
                    "username" : "user_teacher",
                    "email" : "user_teacher@example.com",
                    "password" : "Color.123",
                    "phone":"+22210000002",
                    "is_teacher" : True,
        }
        teacher_data={
                    "subjects":["Mathématiques","Physique Chimie"],
                    "introduction" : "I'm a teacher",
                    "diploma":None,
                    "hourly_wage":"200",
                    "disponibilities" :{"Lundi":["8","9","16","17","18"],"Mardi":["20","21"]}
                }
        user_s_data = {
                    "username" : "green1",
                    "email" : "green1@example.com",
                    "password" : "Color.123",
                    "phone":"+22210000003",
                    "is_student" : True,
                    }
        student_data = {
                    "classe":"0",
                    "speciality" : None,
                    }
        self.user_t = User.objects.create_user(**user_t_data)
        self.teacher = Teacher.objects.create(user=self.user_t,**teacher_data)
        self.user_s = User.objects.create_user(**user_s_data)
        self.student = Student.objects.create(user=self.user_s,**student_data)

    
    def test_login(self):
        data = {
            "username" : "Red",
            "password":"Color.123"
            }
        response = self.client.post(reverse('login'),data)
        try :
            self.assertEqual(response.status_code,status.HTTP_200_OK)
            tprint_OK()
        except:
            tprint_FAIL(str(response.content))

    def test_login_teacher_with_phone(self):
        data = {
            "username" : "+22210000002",
            "password":"Color.123"
            }
        response = self.client.post(reverse('login'),data)
        try :
            self.assertEqual(response.status_code,status.HTTP_200_OK)
            tprint_OK()
        except:
            tprint_FAIL(str(response.content))
            
        
    def test_logout(self):
        #? Nomal auth token
        # self.token = Token.objects.get(user__username="example")
        # self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

        #? simple_jwt token
        self.token = get_tokens_for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token['access'])

        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        tprint_OK()
        