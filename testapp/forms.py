from django import forms
from django.contrib.auth.models import User
from testapp.models import Client

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class ClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields='__all__'






