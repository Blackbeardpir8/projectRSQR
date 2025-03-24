from django.urls import path
from users.views import *
from rest_framework_simplejwt.views import TokenRefreshView

from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # API Endpoints
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),  # <-- Add this!
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    # Test & Frontend Views
    path('about/', about_view, name='about'),
    path('login-page/', login_view, name='login-page'),
    path('register-page/', register_view, name='register-page'),
]

