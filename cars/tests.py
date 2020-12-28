import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

User = get_user_model()


class CarsViewSetTestCase(APITestCase):
  
  # def setUp(self):
  #   self.user = User.objects.create(username="ayser", password="testPassword")
  #   self.token = Token.objects.create(user= self.user)
  #   self.api_authentication()
    

  # def api_authentication(self):
  #   self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

  # def test_authentication(self):
  #   print("Test Authentication")
  #   response = self.client.get("/cars-app/cars")
  #   self.assertEqual(response.status_code, status.HTTP_200_OK)

  # def test_cars_view(self):
    
  #   response = self.client.get("/cars-app/cars")
  #   self.assertEqual(response.status_code, status.HTTP_200_OK)

  def add_new_car_test(self):
   
    data = {
    "plan_name": "First Plan",
    "car_brand": "BMW",
    "car_model": "BMW M4",
    "production_year": "2019",
    "car_body": "4-doors",
    "engine_type": "fuel engine"
    }
    client = APIClient()
    response = client.post('/cars-app/cars/', data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
