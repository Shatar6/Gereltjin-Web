"""
Views for Core app (Homepage, About, Contact)
UPDATED: Added dropdown submenu views
"""
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Homepage view"""
    return render(request, 'core/home.html')

def about(request):
    """About page view"""
    return render(request, 'core/about.html')

def services(request):
    """Services page view"""
    return render(request, 'core/services.html')

def contact(request):
    """Contact page view"""
    return render(request, 'core/contact.html')

def careers(request):
    """Careers page view"""
    return render(request, 'core/careers.html')

# Dropdown submenu pages
def construction(request):
    """Construction & Assembly page"""
    return render(request, 'core/construction.html')

def glass_structure(request):
    """Glass Fabrication page"""
    return render(request, 'core/glass_structure.html')

def windows_doors(request):
    """Windows & Doors page"""
    return render(request, 'core/windows_doors.html')

def rental(request):
    """Rental Services page"""
    return render(request, 'core/rental.html')

def sports_hall(request):
    """Sports Hall page"""
    return render(request, 'core/sports_hall.html')