from django.db import models
import datetime as dt

class Products(models.Model):
    product_name = models.TextField()
    stock = models.IntegerField()
    last_updated = models.DateTimeField(default=dt.datetime.now())

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


class Clients(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=256)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.username}>"
