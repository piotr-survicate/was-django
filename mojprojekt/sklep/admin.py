from django.contrib import admin
from .models import Product
from .models import Order
from .models import OrderedProduct

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderedProduct)
