from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from user_app.models import User ,Student,Teacher

admin.site.register(User, UserAdmin)
admin.site.register(Teacher)
admin.site.register(Student)