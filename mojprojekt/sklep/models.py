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

    def get_total_price(self):
        total = 0
        ordered_products = OrderedProduct.objects.filter(order=self)
        for ordered_product in ordered_products:
            total += ordered_product.amount * ordered_product.product.price
        return total

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    delivery = models.CharField(max_length=100)
    products = models.ManyToManyField("Product", through="OrderedProduct")


class OrderedProduct(models.Model):

    def __str__(self):
        return self.product.name

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    amount = models.IntegerField(default=1)


class Complaint(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=55)
    message = models.CharField(max_length=400)
