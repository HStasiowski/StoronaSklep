from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse


def index_view(request):
    return render(request, "main/index.html")


def render_user_view(request,
                     current_password=None, new_password=None,
                     confirm_new_password=None, unsuccessful_description=None):
    return render(request, "main/user_profile.html", {
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "user_email": request.user.email,
        "predefined_current_password": current_password,
        "predefined_new_password": new_password,
        "predefined_confirm_new_password": confirm_new_password,
        "unsuccessful_description": unsuccessful_description,

    })


def user_view(request):
    if request.user.is_authenticated:
        return render_user_view(request)
    else:
        return redirect(reverse("main:login") + f"?next={reverse('main:user')}")


def change_password(request):
    if request.user.is_authenticated:
        try:
            current_password = request.POST["current-password"]
            new_password = request.POST["new-password"]
            confirm_new_password = request.POST["confirm-new-password"]
        except KeyError:
            return redirect(reverse("main:user"))
        else:
            user = authenticate(request, username=request.user.username, password=current_password)
            if user is None:
                return render_user_view(
                    request,
                    unsuccessful_description="Current password is incorrect.",
                    current_password=current_password,
                    new_password=new_password,
                    confirm_new_password=confirm_new_password
                )
            if new_password == "":
                return render_user_view(
                    request,
                    unsuccessful_description="Password cannot be empty.",
                    current_password=current_password,
                    new_password=new_password,
                    confirm_new_password=confirm_new_password
                )
            if new_password != confirm_new_password:
                return render_user_view(
                    request,
                    unsuccessful_description="Your passwords didn't match.",
                    current_password=current_password,
                    new_password=new_password,
                    confirm_new_password=confirm_new_password
                )
            user_object = User.objects.get(username=request.user.username)
            user_object.set_password(raw_password=new_password)
            user_object.save()
            return HttpResponse("Password has been changed successfully!. "
                                "Login again! http://127.0.0.1:8000/main/user")
    else:
        return redirect(reverse("main:login") + f"?next={reverse('main:user')}")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("main:user")
    else:
        return render(request, "main/user_login.html")


def login_proceed(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]
    except KeyError:
        return redirect("main:login")
    else:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get("next", default=reverse("main:user")))
        else:
            return render(request, "main/user_login.html", {
                "unsuccessful_login": "Bad username or password.",
                "predefined_username": username
            })


def logout_proceed(request):
    logout(request)
    return HttpResponse("Successfully logged out!")
