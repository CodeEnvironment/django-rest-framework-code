from django.db import models
from django.contrib.auth import get_user_model


class Snippets(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=100, blank=True, default='')
  code = models.TextField()
  language = models.CharField(max_length=100)

  class Meta:
    ordering = ['created']
