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

class AccountAdmin(admin.ModelAdmin):
    list_display= ["account_number","username","balance","phone"]
    def username(self,obj):
        return obj.user.username
    def phone(self,obj):
        return obj.user.phone



class TransactionAdmin(admin.ModelAdmin):
    list_display= ["id","username","amount_MRU","phone_number","txn_id","wallet"]
    def id(self,obj):
        return obj.id
    def username(self,obj):
        return obj.account.user.username

    # def save_model(self, request, obj, form, change):
    #     # if 'status' in form.changed_data:
    #     #     if obj.status != xxx (intial data?) and obj.status == 7:
    #     #     # do sth

    #     if obj.can_change and obj.validated:
    #         obj.account.update_balance(obj.amount_MRU)
    #         obj.can_change=False
    #     return super().save_model(request, obj, form, change)



admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Transaction,TransactionAdmin)