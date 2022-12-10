from django.urls import path

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
    path('logout/', views.logout_proceed, name='logout'),
]
