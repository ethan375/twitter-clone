from django.urls import path
from . import views


urlpatterns = [
    path('tweet/new', views.new_tweet, name="new tweet"),
    path('tweet/<int:tweet_id>', views.tweet_detail, name="tweet_detail")
]