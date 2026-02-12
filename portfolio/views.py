"""
Views for Portfolio app (Project Gallery)
"""
from django.shortcuts import render
from django.http import HttpResponse

def portfolio_list(request):
    """Portfolio list view"""
    return render(request, 'portfolio/portfolio_list.html')

def portfolio_detail(request, pk):
    """Portfolio detail view"""
    return HttpResponse(f"Project #{pk} - Coming Soon")