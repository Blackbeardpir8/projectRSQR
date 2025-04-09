from django.urls import path
from .views import qr_profile_view

app_name = "qraccess"

urlpatterns = [
    path("access/<int:user_id>/", qr_profile_view, name="scan"),
]