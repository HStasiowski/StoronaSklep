from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password, ValidationError
from django.shortcuts import render, redirect, reverse


def index_view(request):
    return render(request, "main/index.html")


def about_view(request):
    return render(request, "main/about.html")


def register_view(request):
    return render(request, "main/user_register.html")


def register_success_view(request):
    return render(request, "main/user_register_success.html")


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
            problems = []
            user = authenticate(request, username=request.user.username, password=current_password)
            if user is None:
                problems.append("Current password is incorrect!")
            try:
                validate_password(password=new_password, user=request.user.username)
            except ValidationError as validation_error:
                problems.extend([error.message for error in validation_error.error_list])
            if new_password == "":
                problems.append("New password cannot be empty.")
            if new_password != confirm_new_password:
                problems.append("Your passwords didn't match.")
            if new_password == current_password:
                problems.append("New password cannot be the same as old password.")
            if problems:
                return render_user_view(
                    request,
                    unsuccessful_description=problems,
                    current_password=current_password,
                    new_password=new_password,
                    confirm_new_password=confirm_new_password
                )
            user_object = User.objects.get(username=request.user.username)
            user_object.set_password(raw_password=new_password)
            user_object.save()
            return render(request, "main/user_change_password_success.html")
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
    return render(request, "main/user_logout.html")


def handler404_view(request, exception):
    return render(request, "main/errors/404.html", {}, status=404)


def handler500_view(request, exception=None):
    return render(request, "main/errors/500.html", {}, status=500)


def handler403_view(request, exception=None):
    return render(request, "main/errors/403.html", {}, status=403)


def handler400_view(request, exception=None):
    return render(request, "main/errors/400.html", {}, status=400)
