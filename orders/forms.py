from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_number', 'product_name', 'price', 'quantity',
                  'customer_name', 'address', 'status']