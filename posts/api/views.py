
from rest_framework import viewsets
from rest_framework.response import Response
from posts.models import Posts, PostsRates
from .serializer import PostsSerializer, PostsRatesSerializer
from django.core.mail import send_mail
import threading


class HandleNotifications(threading.Thread):

    def __init__(self, message, subject, recipient_list):
        self.message = message
        self.subject = subject
        self.recipient_list = recipient_list
        threading.Thread.__init__(self)

    def run(self):
        from_email = 'codes.environment@gmail.com'
        send_mail(self.subject, self.message,from_email,self.recipient_list, fail_silently=False)


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer

    def send_email(self, message, subject, recipient_list):
        from_email = 'codes.environment@gmail.com'
        send_mail(subject, message,from_email,recipient_list, fail_silently=False)


    def get_queryset(self):
        posts = Posts.objects.all()
        return posts


    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_rate = PostsRates.objects.create(
            likes=0, dislikes=0)
        new_rate.save()

        new_post = Posts.objects.create(
            post_title=post_data["post_title"], post_body=post_data["post_body"], rates=new_rate)
        new_post.save()
        # self.send_email("this a notification", "Notification",['codes.environment@gmail.com',])
        HandleNotifications("this a notification", "Notification",['codes.environment@gmail.com',]).start()
        serializer = PostsSerializer(new_post)

        return Response(serializer.data)


class PostsRatesViewSet(viewsets.ModelViewSet):
    serializer_class = PostsRatesSerializer

    def get_queryset(self):
        rates = PostsRates.objects.all()
        return rates

