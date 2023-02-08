from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('about/', views.about_view, name='about'),
    path('login/proceed/', views.login_proceed, name='login_proceed'),
    path('user/', views.user_view, name='user'),
    path('user/change_password/', views.change_password, name='change_password'),
    path('user/cart/', views.cart_view, name='cart'),
    path('logout/', views.logout_proceed, name='logout'),
    path('test/', views.test_view, name='test'),
    path('products/', views.products_view, name='products'),
    path('products/<int:product_id>/', views.product_by_id_view, name='product_by_id'),
]
