from re import U
from supplier import models
from django import forms
from django.db.models import fields
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'username', 'password', 'level')
        model = User