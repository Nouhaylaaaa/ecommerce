from django import forms
from .models import Reglement

class ReglementForm(forms.ModelForm):
    class Meta:
        model = Reglement
        fields = ['num_carte', 'montant', 'date_reglement']
        widgets = {
            'montant': forms.HiddenInput(),  # Use a hidden input widget for the montant field
        }