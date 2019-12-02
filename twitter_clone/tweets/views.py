from django.shortcuts import render, redirect
from . models import Tweet
from . forms import NewTweetForm


def tweets(request):
    return render(request, 'placeholder.html')