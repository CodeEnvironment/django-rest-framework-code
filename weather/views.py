
from rest_framework import viewsets
from django.http import HttpResponse
import requests
from weather.models import Forecast
from .serializer import ForecastSerializer


class WeatherViewset(viewsets.ModelViewSet):
  serializer_class = ForecastSerializer

  def get_queryset(self):
    data = Forecast.objects.all()
    return data

  def _get_weather_data(self):
    url = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=14a4121dbd1fb23264f78c57fe690ad6"
    api_request = requests.get(url)

    try:
      api_request.raise_for_status()
      return api_request.json()
    except:
      return None
     
  def save_weather_data(self):
    weather_data = self._get_weather_data()
    print(weather_data)
    if weather_data is not None:
      try:
        weather_object = Forecast.objects.create(temperatuer=weather_data["main"]["temp"], description=weather_data["weather"][0]["description"], city=weather_data["name"])
        weather_data.save()
      except:
        pass
