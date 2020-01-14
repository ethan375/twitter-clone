from django.shortcuts import render, redirect
from . models import Tweet
from . forms import NewTweetForm
from twitterusers.models import TwitterUser
from django.http import HttpResponse


def new_tweet(request):
    if request.method == "POST":
        form = NewTweetForm(request.POST)

        if form.is_valid():
            form = form.cleaned_data
            new_tweet = Tweet.objects.create(
                body=form['body'],
                author=request.user.twitteruser
            )

            user = TwitterUser.objects.filter(id=request.user.id).first()
            user.tweets.add(new_tweet)
            user.save()

        return redirect('/tweet/{}'.format(new_tweet.id))

    else:
        form = NewTweetForm()
        context = {'form': form}

        return render(request, 'tweets/new_tweet.html', context)


def tweet_detail(request, tweet_id):
    tweet = Tweet.objects.filter(id=tweet_id).first()
    context = {'tweet': tweet}

    return render(request, 'tweets/tweet_detail.html', context)


def like_tweet(request, tweet_id):
    tweet = Tweet.objects.filter(pk=tweet_id).first()
    tweet.likes += 1
    tweet.save()
    return HttpResponse("<p>tweet liked</p>")