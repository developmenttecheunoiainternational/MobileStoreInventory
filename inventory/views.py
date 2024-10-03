# inventory/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    Product,
    ProductSerialNumber,
    Supplier,
    Purchase,
    PurchaseItem,
    SalesOrder,
    SalesOrderItem,
)
from .forms import (
    ProductForm,
    ProductSerialNumberForm,
    SupplierForm,
    PurchaseForm,
    PurchaseItemForm,
    SalesOrderForm,
    SalesOrderItemForm,
)
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# --------- Dashboard ---------

@login_required
def dashboard(request):
    total_products = Product.objects.count()
    total_suppliers = Supplier.objects.count()
    total_purchases = Purchase.objects.count()
    total_sales = SalesOrder.objects.count()
    context = {
        'total_products': total_products,
        'total_suppliers': total_suppliers,
        'total_purchases': total_purchases,
        'total_sales': total_sales,
    }
    return render(request, 'inventory/dashboard.html', context)

# --------- Inventory Module ---------

@login_required
def inventory_list(request):
    products_with_stock = []
    
    # Fetch all products and count available stock for each
    products = Product.objects.all()
    for product in products:
        available_stock = product.serial_numbers.filter(status='In Stock').count()
        products_with_stock.append({
            'product': product,
            'available_stock': available_stock
        })
    
    return render(request, 'inventory/inventory_list.html', {'products_with_stock': products_with_stock})

@login_required
def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        serials = request.POST.getlist('serial_number')
        
        if product_form.is_valid():
            product = product_form.save()
            
            # Bulk create serial numbers
            serial_numbers = []
            for serial in serials:
                if serial:  # Ensure serial number is not empty
                    serial_numbers.append(ProductSerialNumber(
                        product=product,
                        serial_number=serial,
                        status='In Stock'
                    ))
            ProductSerialNumber.objects.bulk_create(serial_numbers)
            
            messages.success(request, 'Product and serial numbers added successfully!')
            return redirect('inventory:inventory_list')
    else:
        product_form = ProductForm()
    return render(request, 'inventory/add_product.html', {
        'product_form': product_form,
    })

# --------- Suppliers Module ---------

@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/supplier_list.html', {'suppliers': suppliers})

@login_required
def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier added successfully!')
            return redirect('inventory:supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'inventory/add_supplier.html', {'form': form})

# --------- Purchase Module ---------

@login_required
def purchase_list(request):
    purchases = Purchase.objects.all()
    return render(request, 'inventory/purchase_list.html', {'purchases': purchases})

@login_required
def add_purchase(request):
    PurchaseItemFormSet = modelformset_factory(PurchaseItem, form=PurchaseItemForm, extra=1)

    if request.method == 'POST':
        purchase_form = PurchaseForm(request.POST)
        formset = PurchaseItemFormSet(request.POST)

        if purchase_form.is_valid() and formset.is_valid():
            purchase = purchase_form.save()

            for form in formset:
                purchase_item = form.save(commit=False)
                purchase_item.purchase = purchase
                purchase_item.save()

            return redirect('inventory:purchase_list')
    else:
        purchase_form = PurchaseForm()
        formset = PurchaseItemFormSet(queryset=PurchaseItem.objects.none())

    return render(request, 'inventory/add_purchase.html', {
        'purchase_form': purchase_form,
        'formset': formset
    })
# --------- Sales Module ---------

@login_required
def sales_order_list(request):
    sales_orders = SalesOrder.objects.all()
    return render(request, 'inventory/sales_order_list.html', {'sales_orders': sales_orders})

@login_required
def add_sales_order(request):
    SalesOrderItemFormSet = modelformset_factory(SalesOrderItem, form=SalesOrderItemForm, extra=1)
    
    if request.method == 'POST':
        sales_order_form = SalesOrderForm(request.POST)
        formset = SalesOrderItemFormSet(request.POST, queryset=SalesOrderItem.objects.none())
        
        if sales_order_form.is_valid() and formset.is_valid():
            sales_order = sales_order_form.save()
            
            for form in formset:
                sales_order_item = form.save(commit=False)
                sales_order_item.sales_order = sales_order
                sales_order_item.save()
                
                # Update the status of the serial number to 'Sold'
                if sales_order_item.serial_number:
                    serial = sales_order_item.serial_number
                    serial.status = 'Sold'
                    serial.save()
            
            messages.success(request, 'Sales order created successfully!')
            return redirect('inventory:sales_order_list')
    else:
        sales_order_form = SalesOrderForm()
        formset = SalesOrderItemFormSet(queryset=SalesOrderItem.objects.none())
    
    return render(request, 'inventory/add_sales_order.html', {
        'sales_order_form': sales_order_form,
        'formset': formset
    })
