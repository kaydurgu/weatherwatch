from django.db import models
from user.models import UserProfile
class Sensor(models.Model):
    SENSOR_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Under Maintenance'),
    ]
    SENSOR_LOCATION_CHOICES = [
        ('batken', 'Batken'),
        ('bishkek', 'Bishkek'),
        ('osh', 'Osh'),
    ]
    SENSOR_TYPES = [
        ('thermometer', 'Thermometer'), #temperatrure
        ('hygrometer', 'Hygrometer'), # Humidity
        ('barometer', 'Barometer'),   #pressure
        ('wind_vane:', 'Wind Vane'),  #Wind direction
        ('snow_gauge:', 'Snow Gauge'),  #  Snowfall amount
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=SENSOR_TYPES, default='thermometer')
    model = models.CharField(max_length=100)
    region = models.CharField(max_length=20, choices=SENSOR_LOCATION_CHOICES, default='bishkek')
    location = models.CharField(max_length=100)
    installation_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=SENSOR_STATUS_CHOICES, default='active')
    responsible = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Data(models.Model):

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='data')
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    wind_direction = models.CharField(max_length=250, blank=True, null = True)
    def __str__(self):
        return f"Data for {self.sensor.name}"

class Alert(models.Model):

    SENSOR_SEVERITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
        ('ok', 'Ok'),
    ]
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='alerts')
    description = models.TextField()
    last_timestamp = models.DateTimeField(auto_now=True)
    last_timecheckedby = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    warning_notes = models.TextField(null=True, blank=True)
    severity = models.CharField(max_length=10, choices=SENSOR_SEVERITY_CHOICES, default='ok')