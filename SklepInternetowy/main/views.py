from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404


def index_view(request):
    return render(request, 'main/index.html')


def user_view(request):
    if request.user.is_authenticated:
        return render(request, 'main/user_profile.html', {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'user_email': request.user.email,
        })
    else:
        return redirect(reverse('main:login') + f'?next={reverse("main:user")}')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('main:user')
    else:
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
            return redirect(request.GET.get('next', default=reverse('main:user')))
        else:
            return render(request, 'main/user_login.html', {
                'unsuccessful_login': 'Bad username or password.',
                'predefined_username': username
            })


def logout_proceed(request):
    logout(request)
    return HttpResponse("Successfully logged out!")
