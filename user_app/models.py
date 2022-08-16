from django.db import models
from django.contrib.auth.models import User , AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver 
from rest_framework.authtoken.models import Token
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

# DAYS=("Lundi")),
#       "Mardi")),
#       "Mercredi")),
#       "Jeudi")),
#       "Vendredi")),
#       "Samedi")),
#       "Dimanche")))

DAYS = ("Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche")
def format_disponitbilites(disps):
    """Returns a dict containins all days with their respective dipo if any."""
    disponibilities = dict()
    for day in DAYS:
        try:
            disponibilities[day] = disps[day]
        except :
            disponibilities[day] = []
    return disponibilities

CLASSES = (
    ("99",_("any")),
    ("0", _("Mahdara")),
    ("1", _("1AF")),
    ("2", _("2AF")),
    ("3", _("3AF")),
    ("4", _("4AF")),
    ("5", _("5AF")),
    ("6", _("6AF")),
    ("7", _("1AS")),
    ("8", _("2AS")),
    ("9", _("3AS")),
    ("10", _("4AS")),
    ("11", _("5AS")),
    ("12", _("6AS")),
    ("13", _("7AS")),
)
SPECIALTIES =(
    ("A",_("Literature")),
    ("C",_("Mathématiques")),
    ("D",_("Sciences_Naturelles")),
    ("O",_("Sciences_Religieuses")),
    ("T",_("Technique")),
    )



phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class User(AbstractUser):
    
    phone = models.CharField(unique=True,validators=[phone_regex], max_length=17, blank=True) 
    is_teacher = models.BooleanField(default=False,blank=True,null=True)
    is_student = models.BooleanField(default=False,blank=True,null=True)
    # USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ["phone","email"]
    

class Student(models.Model):

    #? student related fields
    user  = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    classe = models.CharField(max_length=30,null=True,choices=CLASSES)
    speciality = models.CharField(max_length=30,null=True, blank=True,choices=SPECIALTIES)

    def _str_(self):
        return f"STUDENT {self.user.username} | {self.user.phone} | classe : {self.classe + self.speciality}"

class Teacher(models.Model):
    #?Teacher related fields : 
    user  = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    diploma = models.FileField(null=True,blank = True,default=None,upload_to=None,max_length=254,)
    introduction = models.CharField(max_length= 1000)
    hourly_wage = models.PositiveIntegerField(default = 1000)
    subjects = ArrayField(base_field=models.CharField(max_length=50,blank=True),default=list,null=True)
    disponibilities = models.JSONField(null = True)
    avg_rating = models.IntegerField(default = 0)

    def _str_(self):
        return f"TEACHER {self.user.username} | {self.user.phone} | teaches : {self.subjects} | expects {self.hourly_wage}MRU/h"


# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None,created=False,**kwargs):
#     if created : 
#         Token.objects.create(user=instance)