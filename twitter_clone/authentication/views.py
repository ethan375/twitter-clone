from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from . forms import LoginForm


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            form = form.cleaned_data

            user = authenticate(
                username=form['username'],
                password=form['password']
            )

            if user is not None:
                login(request, user)
                return render(request, 'shared/home.html')
    
    else:
        form = LoginForm()
        context = {'form': form}
        
        return render(request, 'auth/login.html', context)
