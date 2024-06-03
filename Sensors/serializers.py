from .models import Sensor, Alert, Data
from rest_framework import serializers



class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = "__all__"
class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = "__all__"
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
    data = DataSerializer(many=True, read_only=True)
    alert = AlertSerializer(many=True, read_only=True)

