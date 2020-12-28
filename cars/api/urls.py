from django.conf.urls import url, include
from .views import CarsAPIView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    url('cars', CarsAPIView.as_view()),
    
]
