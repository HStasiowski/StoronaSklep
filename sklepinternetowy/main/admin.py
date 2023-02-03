from django.contrib import admin
from .models import Products, Promotions, Cart

admin.site.register(Products)
admin.site.register(Promotions)
admin.site.register(Cart)
