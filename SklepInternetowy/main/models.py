from django.db import models
from django.utils import timezone

class Products(models.Model):
    product_name = models.TextField()
    stock = models.IntegerField()
    last_updated = models.DateTimeField(default=timezone.now)

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
