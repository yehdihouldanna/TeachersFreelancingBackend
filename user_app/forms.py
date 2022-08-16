# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.db import transaction
# from .models import User , Student , Teacher , CLASSES,SPECIALTIES

# class CustomUserCreationForm(UserCreationForm):

#     class Meta: 
#         model : User 
#         fields = ('username','email')


# class StudentCreationForm(UserCreationForm):

#     username = forms.CharField(max_length=200 , required = True)
#     phone = forms.CharField(required=True)
#     classe = forms.CharField(max_length=20,choices=CLASSES)
#     speciality = forms.CharField(max_length=30,choices=SPECIALTIES)
#     class Meta(UserCreationForm.Meta): 
#         model : User 

#     @transaction.atomic
#     def data_save(self):
#         user = super().save(commit=False)
#         user.username = self.cleaned_data.get('username')
#         user.phone = self.cleaned_data.get('phone')
#         user.is_student = True
#         user.save()
#         student = Student.objects.create(user = user)
#         student.classe = self.cleaned_data.get('classe')
#         student.speciality = self.cleaned_data.get('speciality')
#         student.save()
#         return student
# class TeacherCreationForm(UserCreationForm):

#     username = forms.CharField(max_length=200 , required = True)
#     phone = forms.CharField(required=True)
#     diploma = forms.FileField(null=True,blank=True,default=None,upload_to=None,max_length=254)
#     introduction = forms.CharField(max_length= 1000)
#     hourly_wage = forms.IntegerField(default = 1000)
#     subjects = forms.JSONField(null=True)
#     disponibilities = forms.JSONField(null = True)
#     class Meta(UserCreationForm.Meta): 
#         model : User 

#     @transaction.atomic
#     def data_save(self):
#         user = super().save(commit=False)
#         user.username = self.cleaned_data.get('username')
#         user.phone = self.cleaned_data.get('phone')
#         user.teacher = True
#         user.save()
#         teacher = Teacher.objects.create(user = user)
#         teacher.classe = self.cleaned_data.get('classe')
#         teacher.speciality = self.cleaned_data.get('speciality')
#         teacher.save()
#         return teacher


# class CustomUserChangeForm(UserChangeForm):

#     class Meta: 
#         model = User
#         fields = ('username','email')
