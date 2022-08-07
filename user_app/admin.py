from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 

# from  .forms import UserChangeForm,UserCreationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *



class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['email','username','phone','date_joined','is_staff']
    search_fields = ['email','username','phone']
    ordering = ['date_joined']

admin.site.register(User,UserAdmin)
admin.site.register(Teacher)
admin.site.register(Student)