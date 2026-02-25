"""
Views for Orders app (Order Management)
"""
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def order_list(request):
    """Order list view"""
    return HttpResponse("Orders List - Coming Soon")

def create_order(request):
    """Create order view"""
    return render(request, 'orders/create_order.html')

def order_detail(request, pk):
    """Order detail view"""
    return HttpResponse(f"Order Detail #{pk} - Coming Soon")

# Customer views
def create_order(request):
    return render(request, 'orders/create_order.html')

# @login_required
def customer_quotes(request):
    return render(request, 'orders/customer_quotes.html')

# @login_required
def customer_profile(request):
    return render(request, 'orders/customer_profile.html')

# Employee views
#@login_required
def portal_dashboard(request):
    # if not request.user.is_staff:
    #     return redirect('core:home')
    return render(request, 'orders/portal_dashboard.html')

# @login_required
def portal_apartments(request):
    # if not request.user.is_staff:
    #     return redirect('core:home')
    return render(request, 'orders/portal_apartments.html')

# @login_required
def portal_machines(request):
    # if not request.user.is_staff:
    #     return redirect('core:home')
    return render(request, 'orders/portal_machines.html')

# @login_required
def portal_vehicles(request):
    # if not request.user.is_staff:
    #     return redirect('core:home')
    return render(request, 'orders/portal_vehicles.html')

# @login_required
def portal_quotations(request):
    # if not request.user.is_staff:
    #     return redirect('core:home')
    return render(request, 'orders/portal_quotations.html')

# Employee action views
# @login_required
def portal_apartment_add(request):
    # if not request.user.is_staff:
    #     return redirect('core:home')
    return render(request, 'orders/portal_apartment_add.html')

# @login_required
def portal_machine_add_maintenance(request):    
    # if not request.user.is_staff:
    #     return redirect('core:home')
    return render(request, 'orders/portal_machine_add_maintenance.html')

# @login_required
def portal_vehicle_add_service(request):
    # if not request.user.is_staff:
    #     return redirect('core:home')
    return render(request, 'orders/portal_vehicle_add_service.html')
