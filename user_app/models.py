from django.db import models
from django.contrib.auth.models import User , AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver 
from rest_framework.authtoken.models import Token
from django.core.validators import MinValueValidator , MaxValueValidator



class CustomUser(AbstractUser):
    phone = models.PositiveIntegerField(null=True,blank=True,validators=[MinValueValidator(10000000),MaxValueValidator(99999999)])
    def __str__(self):
        return self.username
# class Person(CustomUser):
    # phone = models.PositiveIntegerField(null=True,blank=True,validators=[MinValueValidator(10000000),MaxValueValidator(99999999)])
    
# class Student(Person):
#     #? student related fields
#     is_student = models.BooleanField(default=False)


class Teacher(CustomUser):
    #?Teacher related fields : 
    is_teacher = models.BooleanField(default=False)
    diploma = models.FileField(null=True,blank = True,default=None,upload_to=None,max_length=254,)
    subjects = models.JSONField(null=True)
    introduction = models.CharField(max_length= 1000)
    disponibilities = models.JSONField(null = True)
    hourly_wage = models.PositiveIntegerField(default = 1000)


# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None,created=False,**kwargs):
#     if created : 
#         Token.objects.create(user=instance)