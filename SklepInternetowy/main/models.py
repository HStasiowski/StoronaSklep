from django.db import models

class Products(models.Model):
    product_name = models.TextField()
    valid_until = models.DateField()
    stock = models.IntegerField()

    # def __str__(self):
    #     return self.question_text


# class Clients(models.Model):
    # email = models.
