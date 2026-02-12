"""
Views for Services app (Glass Products & Services)
"""
from django.shortcuts import render
from django.http import HttpResponse

def services_list(request):
    """Services list view"""
    return render(request, 'services/services_list.html')

def service_detail(request, slug):
    """Service detail view"""
    return HttpResponse(f"Service: {slug} - Coming Soon")