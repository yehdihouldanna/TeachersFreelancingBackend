import uuid
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from backend.models_basic import Classe, Disponibility, Specialty, Subject

WALLETS = (("Bankily",_("Bankily")),("Masrvi",_("Masrvi")),("Sedad",_("Sedad")),("SiteSpecific",_("SiteSpecific")))
STATUSES = (("Pending",_("Pending")),("Validated",_("Validated")))
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class User(AbstractUser):
    
    phone = models.CharField(_('phone'),unique=True,validators=[phone_regex], max_length=17, blank=True) 
    is_teacher = models.BooleanField(default=False,blank=True,null=True)
    is_student = models.BooleanField(default=False,blank=True,null=True)
    # USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ["phone"]

    def _str_(self):
        nature = "T" if self.is_teacher else "S" if self.is_student else " "
        return f"[{nature}] : { self.username } : { self.phone } "  
    


class Account(models.Model):
    user  = models.OneToOneField(User,on_delete = models.CASCADE,primary_key=True)
    account_number = models.UUIDField(_('account number'),default = uuid.uuid4, editable=False, unique=True)
    balance = models.IntegerField(_('balance'),default = 0,null = False)
    creation_date = models.DateTimeField(_('created at'),auto_now_add=True)

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    def update_balance(self,new_amount):
        self.balance += new_amount
        self.save()
    
    def __repr__(self):
        return f"Compte de {self.user.username}"
    
class Transaction(models.Model):
    def default_platform_account():
        return Account.objects.get(user__username="platform")
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE,blank=True,related_name="transactions")
    destination_account =  models.OneToOneField(Account,default = default_platform_account,on_delete=models.CASCADE,blank=True,null=True,related_name="receiving_account") # ? this is only valid if wallet is intransaction
    amount_MRU = models.IntegerField(_("amount"))
    phone_number = models.CharField(_("phone"),validators=[phone_regex], max_length=17, blank=True) 
    txn_id = models.CharField(_("TXN ID"),max_length=50,blank=True,unique=True)
    wallet = models.CharField(_("Wallet"),max_length=30,choices=WALLETS,default="SiteSpecific")
    creation_date = models.DateTimeField(_('transaction date'),auto_now_add=True)
    is_charging = models.BooleanField(_("is_charging_transaction"),default=False) 
    validated = models.BooleanField(_("validated"),default = False)
    status = models.CharField(_('Status'),max_length=30,choices = STATUSES,default="Pending")
    class Meta:
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')

    can_change = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        can_change = True


class Student(models.Model):
    #TODO the user should now paye in advance for the course.
    #TODO the user makes the order, and after it has been aproved and discussed with the admin he can pay.
    user  = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='user_student')
    classe = models.ForeignKey(Classe,on_delete=models.CASCADE,null=True,blank = True)
    speciality =models.ForeignKey(Specialty,on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def _str_(self):
        return f"STUDENT {self.user.username} | {self.user.phone} | classe : {self.classe + self.speciality}"

class Teacher(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='user')
    diploma = models.FileField(_("diploma"),upload_to="./teachers_diplomes",null=True,blank = True,default=None,max_length=254,)
    introduction = models.CharField(_("introduction"),max_length= 1000, null = True,blank=True)
    hourly_wage = models.PositiveIntegerField(_("hourly wage"),default = 1000 , null=True,blank=True)
    subjects = models.ManyToManyField(Subject, blank=True)
    classes = models.ManyToManyField(Classe,blank=True)
    specialties = models.ManyToManyField(Specialty,blank=True,)
    disponibilities = models.ManyToManyField(Disponibility,blank=True)
    validated = models.BooleanField("validated",default=False)
    avg_rating = models.IntegerField(_("average rating"),default = 0)
    count_ratings = models.IntegerField(default=0,null=True,blank=True)

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')

    def __str__(self):
        return self.user.username

    def update_rating(self,new_rating):
        self.count_ratings +=1
        self.avg_rating= (self.avg_rating+new_rating)/self.count_ratings
        self.save()
    
    def _str_(self):
        return f"TEACHER {self.user.username} | {self.user.phone} | teaches : {self.subjects} | expects {self.hourly_wage}MRU/h"
