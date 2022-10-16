from socket import fromshare
from django import forms 
from .models_basic import SUBJECTS


class SubjectOrderForm(forms.ModelForm):
    subject = forms.ChoiceField(choices=SUBJECTS)
