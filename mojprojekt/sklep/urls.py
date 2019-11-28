from django.urls import path
from . import views

urlpatterns = [
    path('glowna/<str:imie>', views.index),
    path('products/', views.product_list, name='products'),
    path('product/<int:product_id>', views.product, name='product'),
    path('', views.index, name='index'),
]