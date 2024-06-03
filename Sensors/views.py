from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Sensor , Data, Alert
from .serializers import SensorSerializer, DataSerializer, AlertSerializer
# Create your views here.
class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.groups.filter(name='Staff').exists()  or request.user.groups.filter(name='Admin').exists()

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.groups.filter(name='Admin').exists()

class SensorListView(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated and IsStaff]
class SensorDetailView(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated and IsStaff]

class SensorUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class =  SensorSerializer
    permission_classes = [permissions.IsAuthenticated and IsAdmin]
class SensorActiveListView(generics.ListAPIView):
    serializer_class =  SensorSerializer
    permission_classes = [permissions.IsAuthenticated and IsStaff]
    def get_queryset(self):
        return Sensor.objects.filter(status='active')
class SensorInActiveListView(generics.ListAPIView):
    serializer_class =  SensorSerializer
    permission_classes = [permissions.IsAuthenticated and IsStaff]
    def get_queryset(self):
        return Sensor.objects.filter(status='inactive')
class SensorInMaintenanceListView(generics.ListAPIView):
    serializer_class =  SensorSerializer
    permission_classes = [permissions.IsAuthenticated and IsStaff]
    def get_queryset(self):
        return Sensor.objects.filter(status="maintenance")

class SensorDataView(generics.RetrieveAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
class SensorDataUpdateView(generics.UpdateAPIView):
    serializer_class = DataSerializer
    def get_queryset(self):
        return Data.objects.filter(sensor=self.kwargs['pk'])
    permission_classes = [permissions.IsAuthenticated and IsAdmin]
class SensorAlertView(generics.ListAPIView):
    serializer_class =  AlertSerializer
    permission_classes = [permissions.IsAuthenticated and IsStaff]
    def get_queryset(self):
        return Alert.objects.filter(sensor=self.kwargs['pk'])

class SensorAlertUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated and IsStaff]
class SensortAlertListView(generics.ListAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated and IsStaff]