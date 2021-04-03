from django.shortcuts import render
from rest_framework import viewsets
from .models import Album, Track
from .serializer import AlbumSerializer, TrackSerializer


class AlbumViewset(viewsets.ModelViewSet):
  serializer_class = AlbumSerializer

  def get_queryset(self):
    albums = Album.objects.all()
    return albums


class TrackViewset(viewsets.ModelViewSet):
  serializer_class = TrackSerializer

  def get_queryset(self):
    tracks = Track.objects.all()
    return tracks

