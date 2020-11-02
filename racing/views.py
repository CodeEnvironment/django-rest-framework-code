from django.shortcuts import render
from rest_framework import viewsets
from .serializer import DriverSerializer
from .models import Driver
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class DriverViewSet(viewsets.ModelViewSet):
  serializer_class = DriverSerializer
  permission_class = [AllowAny]

  def get_queryset(self):
    driver = Driver.objects.all()
    return driver


