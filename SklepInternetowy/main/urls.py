from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('user', views.user_view, name='user'),
    path('login', views.login_view, name='login'),
    path('login/proceed', views.login_proceed, name='login_proceed'),
    path('logout', views.logout_proceed, name='logout'),
]
