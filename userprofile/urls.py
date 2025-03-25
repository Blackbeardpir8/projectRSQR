from django.urls import path
from .views import *
from . import views

app_name = 'userprofile'

urlpatterns = [
    # API endpoints for profile management (class-based views)
    path('api/profile/', UserProfileView.as_view(), name='user-profile-api'),
    path('api/profile/update/', UserProfileUpdateView.as_view(), name='update-profile-api'),

    # Frontend views for profile pages (function-based views)
    path('profile/', views.profile_view, name='user-profile'),
    path('profile/update/', views.update_profile_view, name='update-profile'),
]
