from django import forms
from .models import teacher

class teacherform(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['name', 'area', 'college']