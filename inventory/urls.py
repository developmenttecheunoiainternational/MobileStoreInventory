# inventory/urls.py

from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Inventory URLs
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/add/', views.add_product, name='add_product'),
    
    # Purchase URLs
    path('purchase/', views.purchase_list, name='purchase_list'),
    path('purchase/add/', views.add_purchase, name='add_purchase'),
    
    # Sales URLs
    path('sales/', views.sales_order_list, name='sales_order_list'),
    path('sales/add/', views.add_sales_order, name='add_sales_order'),
    
    # Suppliers URLs
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/add/', views.add_supplier, name='add_supplier'),
]
