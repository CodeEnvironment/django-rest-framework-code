from django.conf.urls import url, include
from .views import StudentsViewSet, ModulesViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("student", StudentsViewSet, basename="student")
router.register("module", ModulesViewSet, basename="module")


urlpatterns = [
    url('', include(router.urls))
]
