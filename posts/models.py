<<<<<<< HEAD
from django.db import models


class PostsRates(models.Model):
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)


class Posts(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.TextField(max_length=1000)
    rates = models.OneToOneField(
        PostsRates, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.post_title
=======
from django.db import models


class PostsRates(models.Model):
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)


class Posts(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.TextField(max_length=1000)
    rates = models.OneToOneField(
        PostsRates, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.post_title
>>>>>>> 8177ab3bb7908bad888b35267b83d5f301b952e9
