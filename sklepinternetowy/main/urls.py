from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('register/success/', views.register_success_view, name='register_success'),
    path('about/', views.about_view, name='about'),
    path('login/proceed/', views.login_proceed, name='login_proceed'),
    path('user/', views.user_view, name='user'),
    path('user/change_password/', views.change_password, name='change_password'),
    path('user/cart/', views.cart_view, name='cart'),
    path('logout/', views.logout_proceed, name='logout'),
    path('for_testing/', views.for_testing_view, name='for_testing'),
    path('products/', views.products_view, name='products'),
    path('products/produkt_po_wcisnieciu/',views.produkt_po_wcisnieciu_view, name='produkt_po_wcisnieciu'),
]
