from django import forms
from .models import WillDocument

class WillDocumentForm(forms.ModelForm):
    class Meta:
        model = WillDocument
        fields = '__all__'