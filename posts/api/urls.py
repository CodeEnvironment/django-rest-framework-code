<<<<<<< HEAD
from django.conf.urls import url, include
from .views import PostsViewSet, PostsRatesViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("posts", PostsViewSet, basename="posts")
router.register("posts-rates", PostsRatesViewSet, basename="posts-rates")

urlpatterns = [
    url('', include(router.urls))
]
=======
from django.conf.urls import url, include
from .views import PostsViewSet, PostsRatesViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("posts", PostsViewSet, basename="posts")
router.register("posts-rates", PostsRatesViewSet, basename="posts-rates")

urlpatterns = [
    url('', include(router.urls))
]
>>>>>>> 8177ab3bb7908bad888b35267b83d5f301b952e9
