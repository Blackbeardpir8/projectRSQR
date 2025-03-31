from rest_framework import serializers
from .models import EmergencyContact

class EmergencyContactSerializer(serializers.ModelSerializer):
    relation_display = serializers.CharField(source='get_relation_display', read_only=True)

    class Meta:
        model = EmergencyContact
        fields = ['id', 'user', 'name', 'primary_phone', 'alternate_phone', 'relation', 'relation_display']
        extra_kwargs = {'user': {'read_only': True}}
