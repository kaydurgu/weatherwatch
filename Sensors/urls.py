from django.urls import path
from .views import SensorListView, SensorDetailView,SensorUpdateView
urlpatterns = [
    path('', SensorListView.as_view(), name = "sensor-list"), #staff group needed
    path('<int:pk>/', SensorDetailView.as_view(), name = "sensor-detail"),  # Staff group needed
    path('update/<int:pk>/', SensorUpdateView.as_view(), name = "sensor-update"),
]
