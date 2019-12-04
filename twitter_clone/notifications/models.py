from django.db import models
from . twitterusers.models import TwitterUser


class Notification(models.Model):
    body = models.CharField(max_length=280)
    notifcation_from = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    notification_to = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)