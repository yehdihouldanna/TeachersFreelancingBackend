from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import Group
from django_reverse_admin import ReverseModelAdmin

from user_app.models import Account, Transaction, User ,Student,Teacher
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("SchoolAPP admin panel")
admin.site.index_title = _('School App main page')
admin.site.site_title = _('SchoolApp management')

# class TeacherAdmin(ReverseModelAdmin):
#     inline_reverse  = [("user" ,{'fields':['username','phone','email']}),'hourly_wage','validated']
#     inline_type = 'tabular'
#     list_filter = ('validated',)
class TeacherAdmin(admin.ModelAdmin):
    list_display= ["user","validated","hourly_wage","diploma","avg_rating"]
    list_filter = ('validated',)
    # readonly_fields = ["user__username"]
class StudentAdmin(admin.ModelAdmin):
    list_display= ["user","classe","speciality"]
    list_filter = ('classe',)
    # readonly_fields = ["user__username"]


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Account)
admin.site.register(Transaction)