from django import forms
from .models import EmergencyContact

class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ["name", "primary_phone", "alternate_phone", "relation"]
