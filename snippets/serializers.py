from rest_framework import serializers
from .models import Snippets


class SnippetsDetailSerializer(serializers.ModelSerializer):

  class Meta:
    model = Snippets
    fields = ['id', 'title', 'code', 'language']


class SnipppetsListSerialzer(serializers.ModelSerializer):
  snippet_details = serializers.HyperlinkedIdentityField(view_name='snip:snippet-detail')
  

  class Meta:
    model = Snippets
    fields = ['title', 'snippet_details']