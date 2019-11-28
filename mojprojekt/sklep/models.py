from django.db import models

# Create your models here.


class Product(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=400, default='Brak opisu')
    type = models.CharField(max_length=400, default='Brak typu')
    author = models.CharField(max_length=400, default='Autor nieznany')


class Order(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    delivery = models.CharField(max_length=100)