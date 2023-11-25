from django import forms
from django.contrib.auth import authenticate

class customLoginForm(forms.Form):
    ncuenta = forms.IntegerField()
    digitov = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
