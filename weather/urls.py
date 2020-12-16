from django.conf.urls import url, include
from .views import WeatherViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('data', WeatherViewset, basename='weather-data')

urlpatterns = [
    url('', include(router.urls)),
]
