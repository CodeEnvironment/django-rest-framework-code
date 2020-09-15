<<<<<<< HEAD
from rest_framework import serializers
from posts.models import Posts, PostsRates


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ["id", "post_title", "post_body", "rates"]
        depth = 1


class PostsRatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostsRates
        fields = ["id", "likes", "dislikes"]
=======
from rest_framework import serializers
from posts.models import Posts, PostsRates


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ["id", "post_title", "post_body", "rates"]
        depth = 1


class PostsRatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostsRates
        fields = ["id", "likes", "dislikes"]
>>>>>>> 8177ab3bb7908bad888b35267b83d5f301b952e9
