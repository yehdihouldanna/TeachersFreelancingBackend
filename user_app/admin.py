from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from user_app.models import Account, Student, Teacher, Transaction, User

admin.site.site_header = _("SchoolAPP admin panel")
admin.site.index_title = _('School App main page')
admin.site.site_title = _('SchoolApp management')

# class TeacherAdmin(ReverseModelAdmin):
#     inline_reverse  = [("user" ,{'fields':['username','phone','email']}),'hourly_wage','validated']
#     inline_type = 'tabular'
#     list_filter = ('validated',)
class TeacherAdmin(admin.ModelAdmin):
    list_display= ["user","validated","hourly_wage","rating","diploma"]
    list_filter = ('validated',"avg_rating")
    # readonly_fields = ["user__username"]

    def rating(self,obj):
        r = obj.avg_rating
        return "★"*int(r) +"☆"*(5-int(r)) 

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
    list_display= ["id","validated","status","username","amount_MRU","phone_number","txn_id","wallet"]
    def id(self,obj):
        return obj.id
    def username(self,obj):
        return obj.account.user.username

    def save_model(self, request, obj, form, change):
        # if 'status' in form.changed_data:
        #     if obj.status != xxx (intial data?) and obj.status == 7:
        #     # do sth
        if not obj.is_charging and obj.destination_account==Transaction.default_platform_account() and obj.destination_account!=obj.account and obj.account.balance>=obj.amount_MRU:
            obj.destination_account.update_balance(obj.amount_MRU)
            obj.account.update_balance(-obj.amount_MRU)
        elif 'validated' in form.changed_data and obj.status=="Pending":
            obj.account.update_balance(obj.amount_MRU)
            obj.status = "Validated"

        return super().save_model(request, obj, form, change)



admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Transaction,TransactionAdmin)