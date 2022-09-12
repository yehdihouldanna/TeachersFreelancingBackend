from socket import fromshare
from django import forms 
from user_app.models import SUBJECTS


class SubjectOrderForm(forms.ModelForm):
    subject = forms.ChoiceField(choices=SUBJECTS)
