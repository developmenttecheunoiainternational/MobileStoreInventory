# inventory/forms.py

from django import forms
from .models import (
    Product,
    ProductSerialNumber,
    Supplier,
    Purchase,
    PurchaseItem,
    SalesOrder,
    SalesOrderItem,
)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'brand', 'model', 'description']

class ProductSerialNumberForm(forms.ModelForm):
    class Meta:
        model = ProductSerialNumber
        fields = ['serial_number', 'status', 'location']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_person', 'phone', 'email', 'address']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        # fields = ['supplier', 'total_amount']

class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ['product', 'quantity', 'unit_price', 'total_price']
        # fields = ['product', 'quantity', 'unit_price', 'total_price']

class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['customer_name', 'contact_number', 'email', 'total_amount', 'status']

class SalesOrderItemForm(forms.ModelForm):
    class Meta:
        model = SalesOrderItem
        fields = ['product', 'serial_number', 'unit_price', 'total_price']
