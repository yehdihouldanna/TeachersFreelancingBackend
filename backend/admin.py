from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from backend.models import Review,Document, Order,LessonOrder,BookOrder,Book,School,Formation
from backend.models_basic import Subject,Classe,Specialty
from backend.forms import SubjectOrderForm
from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig

class backend(AppConfig):
    name = _('backend')
    verbose_name = _('Orders management')

class SubjectAdmin(admin.ModelAdmin):
    list_display= ["name","pk"]
    form = SubjectOrderForm


class LessonOrderAdmin(admin.ModelAdmin):
    list_display = ["title","username","teacher","unit_price","hours","students_count"]
    def title(self,obj):
        return obj.order.title
    def username(self,obj):
        return obj.order.user.username
    def teacher(self,obj):
        return obj.teacher.user.username

class BookOrderAdmin(admin.ModelAdmin):
    list_display = ["title","username","classe","subject"]
    def title(self,obj):
        return obj.order.title
    def username(self,obj):
        return obj.order.user.username

class BookAdmin(admin.ModelAdmin):
    list_display = ["title","classe","subject","author"]
    
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["title","file","classe","subject","uploader"]
    def uploader(self,obj):
        return obj.order.uploader.username

class SchoolAdmin(admin.ModelAdmin):
    list_display = ["name","phone","adresse"]

class FormationAdmin(admin.ModelAdmin):
    list_display = ["id","school","title","description","start_date","end_date","teacher_name","time"]
    def school(self,obj):
        return obj.school.name

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id","student","lesson","teacher","rating_","content","update"]
    def student(self,obj):
        return obj.review_user.username
    def lesson(self,obj):
        return obj.lesson_order.order.title
    def teacher(self,obj):
        return obj.lesson_order.teacher.user.username
    def rating_(self,obj):
        r = obj.rating
        return "★"*int(r) +"☆"*(5-int(r)) 


admin.site.register(Subject,SubjectAdmin)
admin.site.register(Order)
admin.site.register(LessonOrder,LessonOrderAdmin)
admin.site.register(BookOrder,BookOrderAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Document,DocumentAdmin)
admin.site.register(School,SchoolAdmin)
admin.site.register(Formation,FormationAdmin)
admin.site.register(Review,ReviewAdmin)