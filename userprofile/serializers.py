from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'profile_picture', 'gender', 'date_of_birth', 'address', 'city', 'state', 'zip_code']
