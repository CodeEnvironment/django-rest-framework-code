from rest_framework import serializers
from .models import Album, Track


class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)
    class Meta:
        model = Album
        fields = ['id', 'album_name', 'artist', 'tracks']
       

class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = '__all__'
       