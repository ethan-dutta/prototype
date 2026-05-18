from django import forms
from .models import teacher
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.forms import ValidationError
from .models import Book

emailvalid = RegexValidator(
    regex = r'^(?=.{8,45}$)[\w\.-]+@[\w\.-]+\.\w{2,4}$',
    message = "Name must be no longer than 80 characters and must be a valid email domain",
    code = 'invalid_email'
)
passwordvalid = RegexValidator(
    regex = r'^[a-z]{4,8}[!-+=\d]{4,8}$',
    message = "Password must be between 8 and 20 characters and must contain at least 4 special characters or digits",
    code = 'invalid_password'
)


            
class loginform(AuthenticationForm):
    class Meta:
        model = User
        field = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators.append(emailvalid)
        self.fields['password'].validators.append(passwordvalid)
        # emailfield = User._meta.get_field('username')
        # passwordfield = User._meta.get_field('password')
        # emailfield.validators.append(emailvalid)
        # passwordfield.validators.append(passwordvalid)
#    def clean():
#        cleaned_data = super().clean()

        # erars = []
        # username = cleaned_data.get('username')
        # password = cleaned_data.get('password')
        # if not username:
        #     erars.append(ValidationError("Please enter username"))
        # if not password:
        #     erars.append(ValidationError("Please enter password"))
        # if len(password) < 8 or len(password) > 20:
        #     erars.append(ValidationError("Password must be between 8 and 20 characters"))
        # if len(username) < 8 or len(username) > 20:
        #     erars.append(ValidationError("Username must be between 8 and 20 characters"))
        # return erars


class teacherform(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['name', 'area', 'college']



