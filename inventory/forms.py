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

# Form for managing Product model
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'brand', 'model', 'description']


# Form for managing ProductSerialNumber model
class ProductSerialNumberForm(forms.ModelForm):
    class Meta:
        model = ProductSerialNumber
        fields = ['serial_number', 'status', 'location']


# Form for managing Supplier model
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_person', 'phone', 'email', 'address']


# Form for managing Purchase model
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'  # This includes all fields in the Purchase model
        # If you want to include only specific fields, you can uncomment the following line:
        # fields = ['supplier', 'total_amount']


# Form for managing PurchaseItem model
class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ['product', 'quantity', 'unit_price', 'total_price']
        # fields = ['product', 'quantity', 'unit_price', 'total_price']  # This can be adjusted as per your needs


# Form for managing SalesOrder model
class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['customer_name', 'contact_number', 'email', 'total_amount', 'status']


# Form for managing SalesOrderItem model
class SalesOrderItemForm(forms.ModelForm):
    class Meta:
        model = SalesOrderItem
        fields = ['product', 'serial_number', 'unit_price', 'total_price']
