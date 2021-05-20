from .models import Snippets
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SnippetsDetailSerializer, SnipppetsListSerialzer
from rest_framework.pagination import LimitOffsetPagination
from userapp.serializer import UserDetailsSerializer
from django.contrib.auth import get_user_model

User  = get_user_model()


class SnippetsListView(ListAPIView):
  queryset = Snippets.objects.all()
  serializer_class = SnipppetsListSerialzer
  pagination_class = LimitOffsetPagination


class SnippetsDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Snippets.objects.all()
  serializer_class = SnippetsDetailSerializer


class UserDetails(RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserDetailsSerializer
