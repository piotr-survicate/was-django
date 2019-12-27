from django.contrib import admin
from .models import Product, Order, OrderedProduct, Complaint, Opinion

admin.site.register(Product)
admin.site.register(Order)

admin.site.register(OrderedProduct)

admin.site.register(Complaint)

admin.site.register(Opinion)
# Register your models here.
