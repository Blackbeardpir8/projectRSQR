from django.contrib import admin
from .models import MedicalDetail

@admin.register(MedicalDetail)
class MedicalDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_type', 'primary_doctor_name', 'primary_doctor_contact')
    search_fields = ('user__email', 'medical_conditions', 'allergies', 'primary_doctor_name')
    list_filter = ('blood_type',)
