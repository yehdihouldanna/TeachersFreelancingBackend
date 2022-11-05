from django.db import models
from django.utils.translation import gettext_lazy as _

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
    ("0",_("Autre")),
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

DAYS =(
    ("Lundi",_("Lundi")),
    ("Mardi",_("Mardi")),
    ("Mercredi",_("Mercredi")),
    ("Jeudi",_("Jeudi")),
    ("Vendredi",_("Vendredi")),
    ("Samdi",_("Samdi")),
    ("Dimanche",_("Dimanche")),
    )

class Specialty(models.Model):
    name = models.CharField(_('specialty'),max_length=50,choices=SPECIALTIES,primary_key=True)
    
    class Meta:
        verbose_name = _('Specialty')
        verbose_name_plural = _('Specialties')
    def __str__(self):
        return self.name

class Classe(models.Model):
    name = models.CharField(_('classe'),max_length=25,choices=CLASSES,primary_key=True)
    
    class Meta:
        verbose_name = _('Classe')
        verbose_name_plural = _('Classes')
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(_('subject'),max_length=25,choices=SUBJECTS,primary_key=True)
    
    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')
    def __str__(self):
        return self.name

class Disponibility(models.Model):
    name = models.CharField(_('day'),max_length=25,choices=DAYS,primary_key=True)
    
    class Meta:
        verbose_name = _('Disponibility')
        verbose_name_plural = _('Disponibilities')
    def __str__(self):
        return self.name