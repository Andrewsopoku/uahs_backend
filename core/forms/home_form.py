from django import forms
from django.forms import ModelForm

__author__ = 'andrews'


class LoginForm(forms.Form):
    username = forms.CharField(label="username", required=True, max_length=30,widget=forms.TextInput(attrs={'class': "form-control"}),)
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput(attrs={'class': "form-control"}),)
    remember_me = forms.BooleanField(label="Remember me", required=False)
