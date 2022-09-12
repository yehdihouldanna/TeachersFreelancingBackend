from django.db import models
# Create your models here.
from user_app.models import Student,CLASSES,SUBJECTS,phone_regex
from django.utils.translation import gettext_lazy as _
import json

class Subject(models.Model):
    subject = models.CharField(_('subject'),max_length=20,choices=SUBJECTS,primary_key=True)

    def __str__(self):
        return self.subject+"::"+dict(SUBJECTS)[str(self.subject)]

class Order(models.Model):
    title = models.CharField(_('title'),unique=True,max_length=30, blank=True) 
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="requester")
    description = models.CharField(_('description'),max_length=200,blank=True,null=True)
    adresse = models.CharField(_('adresse'),blank=True,null=True,max_length=100)

    def __str__(self):
        return _("student")+f"{self.student.user.first_name} | {self.student.user.phone} " +_('wants')+f" {self.title}"


class LessonOrder(models.Model):
    order = models.OneToOneField(Order,on_delete=models.CASCADE,primary_key=True)
    subject = models.ManyToManyField(Subject)
    hours = models.IntegerField(default = 2,blank = True, null =True)
    unit_price = models.IntegerField(default = 200,blank=True,null= True)
    students_count = models.IntegerField(default=1,blank=True,null=True)

    # def set_subjects(self,subjects_data):
    #     self.subjects=json.dumps(subjects_data)
    # def get_subjects(self):
    #     return json.loads(self.subjects)

    def __str__(self):
        try:
            return self.order.__str__()
        except:
            return "couldn't print LessonOrder"

class DocumentOrder(models.Model):
    order = models.OneToOneField(Order,on_delete=models.CASCADE,primary_key=True)
    classe = models.CharField(_("classe"),max_length=30,null=True,choices=CLASSES)

    def __str__(self):
        try:
            return self.order.__str__()
        except:
            return "couldn't print DocumentOrder"

class Document(models.Model):
    title = models.CharField(_('title'),max_length=50)
    classe = models.CharField(_('classe'),max_length=30,null=True,choices=CLASSES)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

class School(models.Model):
    name = models.CharField(_('name'),max_length=30)
    adresse = models.CharField(_('adresse'),blank=True,null=True,max_length=100)
    phone = models.CharField(_('phone'),unique=True,validators=[phone_regex], max_length=17, blank=True) 

class Formation(models.Model):
    title =  models.CharField(_('title'),unique=True,max_length=30, blank=True) 
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    description = models.CharField(_('description'),max_length=200,blank=True,null=True)
    adresse = models.CharField(_('adresse'),blank=True,null=True,max_length=100)
    teacher_name = models.CharField(_('teacher name'),max_length=50,blank=True,null=True)
    classe = models.CharField(_('classe'),max_length=30,null=True,choices=CLASSES)
    start_date = models.DateField(_('start date'),blank=True,null=True)
    end_date = models.DateField(_('end date'),blank=True,null=True)
    time = models.TimeField(_('time'),blank=True,null=True)

    def __str__(self):
        return _("School")+f"{self.school.name} " +_('organise')+" 1 "+_('cours')+f"{self.title}"