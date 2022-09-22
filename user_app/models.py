import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User , AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver 
from rest_framework.authtoken.models import Token
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
import uuid


DAYS = ("Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche")
def format_disponitbilites(disps):
    """Returns a dict containins all days with their respective disponibilities if any."""
    disponibilities = dict()
    for day in DAYS:
        try:
            disponibilities[day] = disps[day]
        except :
            disponibilities[day] = []
    return disponibilities

CLASSES = (
    ("99",_("any")),
    ("0", _("Mahdhara")),
    ("1AF",_("1AF")),
    ("2AF",_("2AF")),
    ("3AF",_("3AF")),
    ("4AF",_("4AF")),
    ("5AF",_("5AF")),
    ("6AF",_("6AF")),
    ("1AS",_("1AS")),
    ("2AS",_("2AS")),
    ("3AS",_("3AS")),
    ("4AS",_("4AS")),
    ("5AS",_("5AS")),
    ("6AS",_("6AS")),
    ("7AS",_("7AS")),
)
SPECIALTIES =(
    ("A",_("Literature")),
    ("C",_("Mathématiques")),
    ("D",_("Sciences_Naturelles")),
    ("O",_("Sciences_Religieuses")),
    ("T",_("Technique")),
    )

SUBJECTS = (
    ("All",_("Tout")),
    ("Maths",_("Mathématiques")),
    ("Physics_and_Chemistry",_("Physique Chimie")),
    ("Natural_Sciences",_("Sciences Naturelles")),
    ("Arabic",_("Arabe")),
    ("French",_("Français")),
    ("English",_("Anglais")),
    ("Mahdhara",_("Mahdhara")),
    ("Other",_("Autre")),
)

WALLETS = (("Bankily",_("Bankily")),("Masrvi",_("Masrvi")),("Sedad",_("Sedad")),("SiteSpecific",_("SiteSpecific")))

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class User(AbstractUser):
    
    phone = models.CharField(_('phone'),unique=True,validators=[phone_regex], max_length=17, blank=True) 
    is_teacher = models.BooleanField(default=False,blank=True,null=True)
    is_student = models.BooleanField(default=False,blank=True,null=True)
    # USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ["phone","email"]
    
class Account(models.Model):
    user  = models.OneToOneField(User,on_delete = models.CASCADE,primary_key=True)
    account_number = models.UUIDField(_('account number'),default = uuid.uuid4, editable=False, unique=True)
    balance = models.IntegerField(_('balance'),default = 0,null = False)
    creation_date = models.DateTimeField(_('created at'),auto_now_add=True)

    def update_balance(self,new_amount):
        self.balance += new_amount
        self.save()

class Transaction(models.Model):
    def default_platform_account():
        return Account.objects.filter(user__username="platform")[0].pk
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE,blank=True,related_name="transactions")
    destination_account =  models.OneToOneField(Account,default = default_platform_account,on_delete=models.CASCADE,blank=True,null=True,related_name="receiving_account") # ? this is only valid if wallet is intransaction
    amount_MRU = models.IntegerField(_("amount"))
    phone_number = models.CharField(_("phone"),validators=[phone_regex], max_length=17, blank=True) 
    txn_id = models.CharField(_("TXN ID"),max_length=50,blank=True) #* This is the TXN ID provided by mobile wallet such as Bankily.
    wallet = models.CharField(_("Wallet"),max_length=30,choices=WALLETS,default="SiteSpecific")
    creation_date = models.DateTimeField(_('transaction date'),auto_now_add=True)
    is_charging = models.BooleanField(_("is_charging_transaction"),default=False) #? if is charging mean

class Student(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    classe = models.CharField(_("classe"),max_length=30,null=True,choices=CLASSES)
    speciality = models.CharField(_("specialty"),max_length=30,null=True, blank=True,choices=SPECIALTIES)

    def _str_(self):
        return f"STUDENT {self.user.username} | {self.user.phone} | classe : {self.classe + self.speciality}"

class Teacher(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    diploma = models.FileField(_("diploma"),upload_to="./teachers_diplomes",null=True,blank = True,default=None,max_length=254,)
    introduction = models.CharField(_("introduction"),max_length= 1000, null = True,blank=True)
    hourly_wage = models.PositiveIntegerField(_("hourly wage"),default = 1000 , null=True,blank=True)
    #TODO change subject to manytomany field to solve the problem of multiple entries (it can solve the problem of multiple subjects)
    subjects = ArrayField(base_field=models.CharField(_("subjects"),max_length=50,blank=True),default=list,null=True)
    disponibilities = models.JSONField(_("disponibilities"),null = True)
    validated_account = models.BooleanField("validated_account",default=False)
    avg_rating = models.IntegerField(_("average rating"),default = 0)

    def _str_(self):
        return f"TEACHER {self.user.username} | {self.user.phone} | teaches : {self.subjects} | expects {self.hourly_wage}MRU/h"


# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None,created=False,**kwargs):
#     if created : 
#         Token.objects.create(user=instance)