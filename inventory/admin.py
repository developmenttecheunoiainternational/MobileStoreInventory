# inventory/admin.py

from django.contrib import admin
from .models import (
    Product,
    ProductSerialNumber,
    Supplier,
    Purchase,
    PurchaseItem,
    SalesOrder,
    SalesOrderItem,
)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'model', 'category', 'created_at')
    search_fields = ('name', 'brand', 'model', 'category')

@admin.register(ProductSerialNumber)
class ProductSerialNumberAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'product', 'status', 'location', 'created_at')
    search_fields = ('serial_number', 'product__name')
    list_filter = ('status',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone', 'email', 'created_at')
    search_fields = ('name', 'contact_person', 'phone', 'email')

class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 1

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'purchase_date', 'total_amount', 'created_at')
    search_fields = ('supplier__name',)
    inlines = [PurchaseItemInline]

class SalesOrderItemInline(admin.TabularInline):
    model = SalesOrderItem
    extra = 1

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'sales_date', 'total_amount', 'status', 'created_at')
    search_fields = ('customer_name', 'contact_number', 'email')
    list_filter = ('status',)
    inlines = [SalesOrderItemInline]
