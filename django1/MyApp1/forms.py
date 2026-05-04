from django import forms
from .models import teacher
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class loginform(AuthenticationForm):
    class Meta:
        model = User
        field = ['username', 'password']


class teacherform(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['name', 'area', 'college']

