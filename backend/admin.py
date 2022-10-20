from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from backend.models import Document, Order,LessonOrder,BookOrder,Book,School,Formation
from backend.models_basic import Subject,Classe,Specialty
from backend.forms import SubjectOrderForm
from django.utils.translation import gettext_lazy as _
# class LessonOrderAdmin(admin.ModelAdmin):
#     fields = ('subject')
#     form = LessonOrderForm
class SubjectAdmin(admin.ModelAdmin):
    list_display= ["name","pk"]
    form = SubjectOrderForm

from django.apps import AppConfig

class backend(AppConfig):
    name = _('backend')
    verbose_name = _('Orders management')

class LessonOrderAdmin(admin.ModelAdmin):
    list_display = ["username","teacher","unit_price","hours","students_count"]
    def username(self,obj):
        return obj.order.user.username
    def teacher(self,obj):
        return obj.teacher.user.username
    


admin.site.register(Subject,SubjectAdmin)
admin.site.register(Order)
admin.site.register(LessonOrder,LessonOrderAdmin)
admin.site.register(BookOrder)
admin.site.register(Book)
admin.site.register(Document)
admin.site.register(School)
admin.site.register(Formation)