from pyclbr import Class

from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request, imie):
    return render(request, "sklep/glowna.html", {
        "imie_klienta": imie
    })



def product_list(request):
    products = Product.objects.order_by('id')
    context = {'products': products}

    return render(
        request,
        "sklep/list.html",
        context)


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}

    return render(
        request,
        "sklep/product.html",
        context)

def index(request):

    return render(
        request,
        "sklep/index.html")