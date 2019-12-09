from django.db import models
from django.contrib.auth.models import User
from tweets.models import Tweet


class TwitterUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tweets = models.ManyToManyField('tweets.Tweet')
    follwers = models.ManyToManyField('TwitterUser', related_name='users_followers')
    following = models.ManyToManyField('TwitterUser', related_name='users_following')
