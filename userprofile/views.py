# userprofile/views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse

# View to get the user profile
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile = UserProfile.objects.get(user=request.user)
            serializer = UserProfileSerializer(profile)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Profile not found"
                }, status=status.HTTP_404_NOT_FOUND)

# View to create or update the user profile
class UserProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            profile = UserProfile.objects.get(user=request.user)
            serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        except UserProfile.DoesNotExist:
            serializer = UserProfileSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.views import APIView

@login_required
def profile_view(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, 'userprofile/profile.html', {'userprofile': profile, 'user': request.user})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def update_profile_view(request):
    # Ensure the user has a profile, create one if it doesn't exist
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile.date_of_birth = request.POST.get('date_of_birth', None)
        profile.address = request.POST.get('address', '')
        profile.city = request.POST.get('city', '')
        profile.state = request.POST.get('state', '')
        profile.zip_code = request.POST.get('zip_code', '')
        profile.gender = request.POST.get('gender', '')

        if request.FILES.get('profile_picture'):
            profile.profile_picture = request.FILES['profile_picture']

        profile.save()

        print(f"User: {request.user}, Profile: {profile}, Created: {created}")

        return render(request, 'userprofile/profile.html', {'userprofile': profile})  # ✅ No new request# Redirect to the profile page

    return render(request, 'userprofile/update_profile.html', {'userprofile': profile})

