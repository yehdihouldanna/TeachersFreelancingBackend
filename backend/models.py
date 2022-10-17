from django.db import models
# Create your models here.
from user_app.models import User,Student,phone_regex
from .models_basic import *
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    title = models.CharField(_('title'),max_length=30, blank=True) 
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="requester")
    description = models.CharField(_('description'),max_length=200,blank=True,null=True)
    adresse = models.CharField(_('adresse'),blank=True,null=True,max_length=100)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class LessonOrder(models.Model):
    order = models.OneToOneField(Order,on_delete=models.CASCADE,primary_key=True)
    subjects = models.ManyToManyField(Subject,blank=True)
    hours = models.IntegerField(default = 2,blank = True, null =True)
    unit_price = models.IntegerField(default = 200,blank=True,null= True)
    students_count = models.IntegerField(default=1,blank=True,null=True)
    classes = models.ManyToManyField(Classe,blank=True)
    class Meta:
        verbose_name = _('LessonOrder')
        verbose_name_plural = _('LessonOrders')

    def __str__(self):
        return self.order.__str__()
        

class Document(models.Model):
    """ This model class is for the public domcuments published by professors"""
    title = models.CharField(_('title'),max_length=50)
    classe = models.CharField(_('classe'),max_length=30,null=True,choices=CLASSES)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    file = models.FileField(_("document_file"),upload_to="./document_files",max_length=254,)
    uploader = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name = "uploader")
    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Document')

class Book(models.Model):
    title = models.CharField(_('title'),max_length=50)
    classe = models.CharField(_('classe'),max_length=30,null=True,choices=CLASSES)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    # file = models.FileField(_("book_file"),upload_to="./book_files",null=True,blank = True,default=None,max_length=254,)
    author = models.CharField(_("author_name"),max_length = 50,blank=True,null=True)

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

class BookOrder(models.Model):
    order = models.OneToOneField(Order,on_delete=models.CASCADE,primary_key=True)
    classe = models.ForeignKey(Classe,on_delete=models.CASCADE,blank=True,null=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE , null=True,blank=True)
    books = models.ManyToManyField(Book,blank=True)

    
    def __str__(self):
        return self.order.__str__()

    class Meta:
        verbose_name = _('BookOrder')
        verbose_name_plural = _('BookOrders')


class School(models.Model):
    name = models.CharField(_('name'),max_length=30)
    adresse = models.CharField(_('adresse'),blank=True,null=True,max_length=100)
    phone = models.CharField(_('phone'),unique=True,validators=[phone_regex], max_length=17, blank=True) 

    class Meta:
        verbose_name = _('School')
        verbose_name_plural = _('Schools')

class Formation(models.Model):
    title =  models.CharField(_('title'),unique=True,max_length=100, blank=True) 
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    description = models.CharField(_('description'),max_length=200,blank=True,null=True)
    teacher_name = models.CharField(_('teacher name'),max_length=50,blank=True,null=True)
    classe = models.ForeignKey(Classe,on_delete=models.CASCADE,blank=True,null=True)
    start_date = models.DateField(_('start date'),blank=True,null=True)
    end_date = models.DateField(_('end date'),blank=True,null=True)
    time = models.TimeField(_('time'),blank=True,null=True)

    class Meta:
        verbose_name = _('Formation')
        verbose_name_plural = _('Formations')

    def __str__(self):
        return f"{self.title} | {self.school.name}"