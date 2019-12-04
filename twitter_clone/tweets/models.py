from django.db import models 


class Tweet(models.Model):
    body = models.CharField(max_length=280)
    author = models.ForeignKey('TwitterUser', on_delete=models.CASCADE, null=True, blank=True)
    likes = models.IntegerField()
