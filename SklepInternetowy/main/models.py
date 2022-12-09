from django.db import models

class Products(models.Model):
    product_name = models.TextField()
    valid_until = models.DateField()
    stock = models.IntegerField()


