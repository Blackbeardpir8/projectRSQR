"""
URL configuration for RescueQR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

# Global Home View (For base.html and home.html)
def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    path('', home_view, name='home'),  # Global home page
    path('users/', include('users.urls', namespace='users')),  # Include users app URLs
    path('userprofile/', include(('userprofile.urls', 'userprofile'), namespace='userprofile')),
    path('medical/', include('medical.urls', namespace='medical')),  # Include medical app URLs
    path("emergency/", include("emergency.urls",namespace='emergency')),  # Include userprofile app URLs
    path("qr_code/", include("qrcode_app.urls")),
    path('qr/', include('qraccess.urls', namespace='qraccess')),
]


# Serving media files (only in development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
