from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def user(request):
    return render(request, 'main/user_profile.html')


def login(request):
    return render(request, 'main/user_login.html')
