from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        fields = ('name', 'no_hp', 'address')
        model  = Supplier