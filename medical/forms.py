from django import forms
from .models import MedicalDetail

class MedicalDetailForm(forms.ModelForm):
    class Meta:
        model = MedicalDetail
        fields = [
            "blood_type", "medical_conditions", "allergies", "past_surgeries", 
            "current_medications", "primary_doctor_name", "primary_doctor_contact", 
            "medical_document", "insurance_document"
        ]
