from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import SnippetsDetailView, SnippetsListView, UserDetails

urlpatterns = [
  path('snippets/', SnippetsListView.as_view(), name='snippet-list'),
  path('snippets/<int:pk>/', SnippetsDetailView.as_view(), name='snippet-detail')
 
]