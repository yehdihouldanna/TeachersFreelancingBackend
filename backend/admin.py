from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from backend.models import Order,LessonOrder,DocumentOrder,Document,School,Formation, Subject
from backend.forms import SubjectOrderForm

# class LessonOrderAdmin(admin.ModelAdmin):
#     fields = ('subject')
#     form = LessonOrderForm
class SubjectAdmin(admin.ModelAdmin):
    fields = ('subject')
    form = SubjectOrderForm

admin.site.register(Subject)
admin.site.register(Order)
admin.site.register(LessonOrder)
admin.site.register(DocumentOrder)
admin.site.register(Document)
admin.site.register(School)
admin.site.register(Formation)