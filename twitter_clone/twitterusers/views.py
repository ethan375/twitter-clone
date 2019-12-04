from django.shortcuts import render
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

            return render(request, 'placeholder.html')
    else:
        form = NewTwitterUser()
        context = {'form': form}

        return render(request, 'users/new_user.html', context)


    def login_user(request):
        if request.method == 'POST':
            pass
        else:
            