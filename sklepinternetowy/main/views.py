from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from .forms import RegisterForm
from .models import Products, Cart


def index_view(request):
    return render(request, "main/index.html")


def product_by_id_view(request, product_id: int):
    try:
        product = Products.objects.get(pk=product_id)
    except Products.DoesNotExist:
        return HttpResponse(content="Produkt nie znaleziono...", status=404)
    else:
        return render(
            request,
            "main/product_by_id.html",
            {
                "product": product,
                "price": f"{product.price:.2f}"
            }
        )


def cart_view(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            try:
                cart_objects = Cart.objects.filter(user_id=request.user.id).all()
            except Cart.DoesNotExist:
                return render(request, "main/cart.html")
            else:
                return render(request, "main/cart.html", {"cart_objects": cart_objects})
        elif request.method == "POST":
            try:
                product_id = int(request.POST.get("product_id"))
            except (KeyError, ValueError):
                return HttpResponse(status=500)
            else:
                try:
                    cart_entry = Cart.objects.get(user_id=request.user.id, product_id=product_id)
                except Cart.DoesNotExist:
                    cart_entry = Cart.objects.create(
                        user_id=request.user,
                        product_id_id=product_id,
                        count_items=1
                    )
                    cart_entry.save()
                else:
                    cart_entry.count_items += 1
                    cart_entry.save()
                return render(request, "main/cart.html", {"products": Cart.objects.filter(user_id=request.user.id).all()})
    else:
        return render(request, "main/cart.html", {"not_authenticated": True})


def products_view(request):
    all_products = Products.objects.all()
    n_products = len(all_products)
    n_rows = n_products // 3 if n_products % 3 == 0 else n_products // 3 + 1
    rows = [all_products[(row_id * 3):((row_id + 1) * 3)] for row_id in range(n_rows)]
    return render(
        request, "main/products.html",
        {
            "all_products": all_products,
            "n_products": n_products,
            "n_rows": n_rows,
            "rows": rows
        }
    )


def test_view(request):
    return render(request, "main/index.html")


def about_view(request):
    return render(request, "main/about.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse("main:user"))
    else:
        if request.method == "POST":
            # User has submitted his form
            form = RegisterForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                user_email = form.cleaned_data["user_email"]
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                try:
                    user_object = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        email=user_email,
                        username=username,
                        password=password,
                    )
                except IntegrityError:
                    form.add_error(
                        "username",
                        ValidationError(
                            "Username %(username)s is already taken.",
                            params={"username": username}
                        ))
                else:
                    user_object.save()
                    return render(request, "main/user_register_success.html")
        else:
            # User has opened registration page
            form = RegisterForm()

        # Render a new registration page or fulfill old data with errors
        return render(request, "main/user_register.html", {"form": form})


def render_user_view(request,
                     current_password=None, new_password=None,
                     confirm_new_password=None, unsuccessful_description=None):
    return render(request, "main/user_profile.html", {
        "user": request.user,
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
            return HttpResponse(status=500)
        else:
            problems = []
            user = authenticate(request, username=request.user.username, password=current_password)
            if user is None:
                problems.append("Current password is incorrect!")
            try:
                validate_password(password=new_password, user=request.user.username)
            except ValidationError as validation_error:
                problems.extend([error.messages[0] for error in validation_error.error_list])
            if new_password == "":
                problems.append("New password cannot be empty.")
            if new_password != confirm_new_password:
                problems.append("Your passwords doesn't match.")
            if new_password == current_password:
                problems.append("New password cannot be the same as the old one.")
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
        return HttpResponse(status=500)
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
