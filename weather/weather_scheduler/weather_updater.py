from apscheduler.schedulers.background import BackgroundScheduler
from weather.views import WeatherViewset

def start():
  scheduler = BackgroundScheduler()
  weather = WeatherViewset()
  scheduler.add_job(weather.save_weather_data, "interval", minutes=1,id="weather_001",replace_existing=True)
  scheduler.start()