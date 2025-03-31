from django.db import models
from users.models import CustomUser

class MedicalDetail(models.Model):
    # Blood Type Choices
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="medical_detail")
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES, blank=True, null=True)
    
    medical_conditions = models.TextField(blank=True, null=True)  # Store conditions like Diabetes, Hypertension
    allergies = models.TextField(blank=True, null=True)  # Store allergies like Peanuts, Dust
    past_surgeries = models.TextField(blank=True, null=True)  # Store past surgeries
    current_medications = models.TextField(blank=True, null=True)  # List of current medications
    
    primary_doctor_name = models.CharField(max_length=255, blank=True, null=True)
    primary_doctor_contact = models.CharField(max_length=20, blank=True, null=True)

    # Medical and Insurance Documents
    medical_document = models.FileField(upload_to="medical_documents/", blank=True, null=True)
    insurance_document = models.FileField(upload_to="insurance_documents/", blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - Medical Details"
