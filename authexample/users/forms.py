from django.contrib.auth.forms import UserCreationForm
from . import models
from django import forms


class SignUpFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['user', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)