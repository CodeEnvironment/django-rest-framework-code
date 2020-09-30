from rest_framework import viewsets
from rest_framework.response import Response
from posts.models import Posts, PostsRates
from .serializer import PostsSerializer, PostsRatesSerializer


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer

    def get_queryset(self):
        posts = Posts.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_rate = PostsRates.objects.create(
            likes=post_data["rates"]["likes"], dislikes=post_data["rates"]["dislikes"])
        new_rate.save()

        new_post = Posts.objects.create(
            post_title=post_data["post_title"], post_body=post_data["post_body"], rates=new_rate)
        new_post.save()

        serializer = PostsSerializer(new_post)

        return Response(serializer.data)


class PostsRatesViewSet(viewsets.ModelViewSet):
    serializer_class = PostsRatesSerializer

    def get_queryset(self):
        rates = PostsRates.objects.all()
        return rates
