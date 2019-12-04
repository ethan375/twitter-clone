from django.db import models
from django.contrib.auth import User
from . tweets.models import Tweet


class TwitterUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweets = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True, blank=True)
