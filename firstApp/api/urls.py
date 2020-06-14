from django.conf.urls import url, include
from .views import firstFunction, deleteObjects
from rest_framework.routers import DefaultRouter
from .views import CarSpecsViewset

router = DefaultRouter()
router.register('car-specs', CarSpecsViewset, basename='car-specs')


urlpatterns = [
    url('first', firstFunction),
    url('delete', deleteObjects),
    url('', include(router.urls))
]
