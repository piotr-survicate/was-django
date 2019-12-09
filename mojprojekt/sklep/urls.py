from django.urls import path
from . import views

urlpatterns = [
    path('glowna/<str:imie>', views.index),
    path('products/', views.product_list, name='products'),
    path('product/<int:product_id>', views.product, name='product'),
    path('orders/', views.order_list, name='orders'),
    path('', views.index, name='index'),
    path('orders/<int:order_id>', views.order_details),
    path('order/', views.order),
    path('complaint/', views.complaint),
    path('complaint/<int:complaint_id>', views.complaint_details),
]