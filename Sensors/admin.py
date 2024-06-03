from django.contrib import admin
from .models import Data, Alert, Sensor
# Register your models here.

admin.site.register(Data)
admin.site.register(Alert)
admin.site.register(Sensor)
