from rest_framework import serializers
from .models import MedicalDetail

class MedicalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetail
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}
