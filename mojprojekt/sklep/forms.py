from django.forms import ModelForm
from .models import Order
from .models import Complaint


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'delivery']


class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'message']
