from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import Group
from django_reverse_admin import ReverseModelAdmin

from user_app.models import Account, Transaction, User ,Student,Teacher



admin.site.site_header = "La page admin de SchoolAPP"

# class TeacherAdmin(ReverseModelAdmin):
#     inline_reverse  = [("user" ,{'fields':['username','phone','email']}),'hourly_wage','validated']
#     inline_type = 'tabular'
#     list_filter = ('validated',)
class TeacherAdmin(admin.ModelAdmin):
    #TODO find a way to add the related fields of user in the teacher list view
    list_display= ["user","validated","hourly_wage","diploma"]
    list_filter = ('validated',)
    # readonly_fields = ["user__username"]


admin.site.unregister(Group)

admin.site.register(User, UserAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student)
admin.site.register(Account)
admin.site.register(Transaction)