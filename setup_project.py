#? This is the setup file for the project after all the installations 
# execute this file using django shell :
#       $ python manage.py shell
#       >>> exec(open("setup_project.py").read())
#

from backend.models_basic import Disponibility, Subject,Specialty,Classe,CLASSES,SPECIALTIES,SUBJECTS,DAYS
from user_app.models import Account, User
from termcolor import cprint

print("Creating the 'platform' base user ... ",end=" ")

try :
    User.objects.create_superuser(username = 'platform',email= 'platform@gmail.com' ,phone =  '+22299999999', password ='platform')
    cprint("OK !",color="green",attrs=["bold"])
except :
    cprint("SKIPPED" , color= "blue",attrs=["bold"], end = " ")
    print("User 'platform' already exist !")

print("Creating the base account for platform ...")
try :
    Account.objects.create(user = User.objects.get(username='platform'))
    cprint("OK !",color="green",attrs=["bold"])
except :
    cprint("SKIPPED" , color= "blue",attrs=["bold"], end = " ")
    print(" Account for user 'platform' already exist !")

print("Creating the basic choices for Classes, Subjects , and specialties : ...")
for subject in SUBJECTS :
    print(f"Creating subject '{subject[0]}' ... ",end = "")
    try :
        Subject.objects.create(name=subject[0])
        cprint("OK !",color="green",attrs=["bold"])
    except :
        cprint("SKIPPED" , color= "blue",attrs=["bold"] , end = " ")
        print(" already exist !")
for specialty in SPECIALTIES :
    print(f"Creating specialty '{specialty[0]}' ... ",end = "")
    try : 
        Specialty.objects.create(name=specialty[0])
        cprint("OK !",color="green",attrs=["bold"])
    except :
        cprint("SKIPPED" , color= "blue",attrs=["bold"], end = " ")
        print(" already exist !")
for classe in CLASSES :
    print(f"Creating classe '{classe[0]}' ... ",end = "")
    try:
        Classe.objects.create(name=classe[0])
        cprint("OK !",color="green",attrs=["bold"])
    except :
        cprint("SKIPPED" , color= "blue",attrs=["bold"], end = " ")
        print(" already exist !")
for day in DAYS :
    print(f"Creating diponibility '{day[0]}' ... ",end = "")
    try:
        Disponibility.objects.create(name=day[0])
        cprint("OK !",color="green",attrs=["bold"])
    except :
        cprint("SKIPPED" , color= "blue",attrs=["bold"], end = " ")
        print(" already exist !")