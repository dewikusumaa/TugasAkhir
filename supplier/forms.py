from django import forms
from django.db import models
from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    name = forms.CharField()
    no_hp = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = ('name', 'no_hp', 'address')
        models = Supplier