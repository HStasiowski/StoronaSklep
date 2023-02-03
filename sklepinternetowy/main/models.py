from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Products(models.Model):
    product_name = models.TextField()
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    last_updated = models.DateTimeField(default=timezone.now)
    product_img = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.product_name


class Promotions(models.Model):
    promo_name = models.TextField()
    promo_description = models.TextField()
    promo_start = models.DateTimeField()
    promo_end = models.DateTimeField()
    promo_products = models.ManyToManyField(Products)

    def __str__(self):
        return self.promo_name


class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    count_items = models.IntegerField(default=1)

    class Meta:
        unique_together = ('user_id', 'product_id',)
