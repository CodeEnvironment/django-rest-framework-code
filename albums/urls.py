from django.conf.urls import url, include
from .views import AlbumViewset, TrackViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("album", AlbumViewset, basename="album")
router.register("track", TrackViewset, basename="track")

urlpatterns = [
    url('', include(router.urls))
]
