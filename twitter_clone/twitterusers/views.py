from django.shortcuts import render, redirect
from tweets.models import Tweet
from . models import TwitterUser
from . forms import NewTwitterUser
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout


def create_new_user(request):
    if request.method == "POST":
        form = NewTwitterUser(request.POST)

        if form.is_valid():
            form = form.cleaned_data

            user = User.objects.create_user(
                username=form['username'],
                password=form['password']
            )

            TwitterUser.objects.create(
                username=form['username'],
                user=user
            )

            return redirect('/')
    else:
        form = NewTwitterUser()
        context = {'form': form}

        return render(request, 'users/new_user.html', context)


def user_detail(request, user_id):
    user = TwitterUser.objects.filter(id=user_id).first()
    tweets = Tweet.objects.filter(author=user.id)

    context = {
        'user': user,
        'tweets': tweets,
        }
    try:
        context['loggedin_user'] = request.user.twitteruser.id
    except:
        print('some things like didnt work or something ')

    return render(request, 'users/user_detail.html', context)


def follow_user(request, loggedin_user, following_user):
    loggedin_user = TwitterUser.objects.filter(id=loggedin_user).first()
    following_user = TwitterUser.objects.filter(id=following_user).first()

    loggedin_user.following.add(following_user)
    return redirect('/user/{}'.format(following_user.id))    
