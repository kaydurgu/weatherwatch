from django.urls import path
from .views import SensorListView
urlpatterns = [
    path('', SensorListView.as_view(), name = "sensor-list"),
   # path('<int:pk/>', SensorListView.as_view(), name = "sensor-list")
]
