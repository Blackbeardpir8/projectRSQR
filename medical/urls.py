from django.urls import path
from .views import MedicalDetailAPIView, medical_detail_view, update_medical_details

app_name = 'medical'


urlpatterns = [
    # API to get and update medical details
    path('api/medical-details/', MedicalDetailAPIView.as_view(), name='medical-details-api'),
    path("medical-details/", medical_detail_view, name="medical_details"),
    path("update-medical-details/", update_medical_details, name="update_medical_details"),
]
