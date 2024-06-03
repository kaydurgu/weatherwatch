from .models import Sensor, Alert, Data
from rest_framework import serializers


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
