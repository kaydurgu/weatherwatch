from django.urls import path
from .views import (SensorListView, SensorDetailView,SensorUpdateView, SensorActiveListView,
                    SensorInActiveListView,SensorInMaintenanceListView, SensorDataView, SensorDataUpdateView,
                    SensorAlertView)

urlpatterns = [
    path('', SensorListView.as_view(), name = "sensor-list"), #staff group needed
    path('<int:pk>/', SensorDetailView.as_view(), name = "sensor-detail"),  # Staff group needed
    path('update/<int:pk>/', SensorUpdateView.as_view(), name = "sensor-update"), #admin group needed
    path('active/', SensorActiveListView.as_view(), name = "list-of-active"),
    path('inactive/', SensorInActiveListView.as_view(), name = "list-of-inactive"),
    path('inmaintance/', SensorInMaintenanceListView.as_view(), name = "list-of-inactive"),
    #data
    path('data/<int:pk>/', SensorDataView.as_view(), name = "sensor-data"),
    path('data/update/<int:pk>/', SensorDataUpdateView.as_view(), name = 'sensor-data-update'),
    #alerts
    path('alert/<int:pk>/', SensorAlertView.as_view(), name = "sensor-alert-view"),

]
