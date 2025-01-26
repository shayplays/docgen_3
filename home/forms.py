from django import forms
from .models import LegalDocument

class WillForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['name', 'father_name', 'age', 'address', 'executor_name', 'wife_name', 'child_name_1', 'child_name_2', 'flat_no', 'flat_address', 'date', 'month', 'year', 'time']

class LicenseForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['name', 'father_name', 'address', 'date']