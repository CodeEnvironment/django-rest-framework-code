from django.conf.urls import url
from .views import CarsAPIView

urlpatterns = [
    url('cars', CarsAPIView.as_view())
]
