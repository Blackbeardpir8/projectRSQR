from django.urls import path
from users.views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView




app_name = 'users'

urlpatterns = [
    # API Endpoints
    path('api/register/', UserRegistrationView.as_view(), name='user-register'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/profile/', UserProfileView.as_view(), name='user-profile'),

    path("api/user-data/", get_user_complete_data, name="user-data"), # All Data
    path('api/user-data/<int:user_id>/', get_user_complete_data),

    
    # Test & Frontend Views
    path('login-page/', login_view, name='login-page'),
    path('register-page/', register_view, name='register-page'),
    path('logout/', logout_view, name='logout'),
    path('about/', about_view, name='about'),
    path('faq/', faq_view, name='faq'),
    path('privacy-policy/', privacy_policy_view, name='privacy_policy'),
    path('terms-of-service/', terms_of_service_view, name='terms_of_service'),
    path('how-it-works/', how_it_works_view, name='how_it_works'),
]
