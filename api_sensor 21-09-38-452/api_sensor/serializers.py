from rest_framework import serializers
from .models import LeituraSensor

class LeituraSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeituraSensor
        fields = '__all__'
