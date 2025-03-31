from django.urls import path
from .views import generate_qr_code


app_name = 'qrcode_app'

urlpatterns = [
    path("generate/", generate_qr_code, name="generate_qr"),
]