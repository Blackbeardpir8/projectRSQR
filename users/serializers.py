from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    confirm_password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['email', 'phone', 'first_name', 'middle_name', 'last_name', 'password', 'confirm_password', 'role']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password before saving
        user = User.objects.create_user(
            email=validated_data['email'],
            phone=validated_data['phone'],
            first_name=validated_data['first_name'],
            middle_name=validated_data.get('middle_name', ''),
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            role=validated_data.get('role', 'user')
        )
        return user



from rest_framework import serializers
from django.contrib.auth import get_user_model
from userprofile.serializers import UserProfileSerializer
from medical.serializers import MedicalDetailSerializer
from emergency.serializers import EmergencyContactSerializer
from qrcode_app.models import QRCode  # Import QR model

User = get_user_model()

class UserCompleteDataSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source="userprofile", read_only=True)
    medical_details = MedicalDetailSerializer(many=True, read_only=True, source="medicaldetail_set")
    emergency_contacts = EmergencyContactSerializer(many=True, read_only=True, source="emergencycontact_set")
    qr_code = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "email", "phone", "first_name", "middle_name", "last_name", "role", 
                  "profile", "medical_details", "emergency_contacts", "qr_code"]

    def get_qr_code(self, obj):
        """Retrieve QR code URL if it exists."""
        qr = QRCode.objects.filter(user=obj).first()
        return qr.qr_image.url if qr and qr.qr_image else None
