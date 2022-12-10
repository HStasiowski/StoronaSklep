from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404


def index_view(request):
    return render(request, 'main/index.html')


def user_view(request):
    return render(request, 'main/user_profile.html')


def login_view(request):
    return render(request, 'main/user_login.html')


def login_proceed(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
    except KeyError:
        return redirect('main:login')
    else:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:user')
        else:
            return render(request, 'main/user_login.html', {
                'unsuccessful_login': 'Bad username or password.',
                'predefined_username': username
            })
