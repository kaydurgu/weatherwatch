from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Sensor
from .serializers import SensorSerializer
# Create your views here.
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.groups.filter(name='Admin').exists()

class SensorListView(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated and IsAdminOrReadOnly]
#class SensorDetailView(generics.RetrieveAPIView):
#    queryset = Sensor.objects.all()
#    serializer_class = SensorSerializer
#    permission_classes = [permissions.IsAuthenticated]
