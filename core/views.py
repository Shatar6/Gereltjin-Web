"""
Views for Core app (Homepage, About, Contact)
UPDATED: Added dropdown submenu views
"""
import email

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage

def portal_login(request):
    """Portal login page view"""
    return render(request, 'portal/portal_login.html')

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

def portfolio(request):
    """Portfolio page"""
    return render(request, 'portfolio/portfolio_list.html')

def create_order(request):
    """Create Order page view"""
    return render(request, 'portal/create_order.html')

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

# Contact form submission view
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import ContactForm

@require_POST
def contact_submit(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        email = EmailMessage(
            subject=f"Contact: {form.cleaned_data['subject']}",
            body=f"""
        Name: {form.cleaned_data['name']}
        Email: {form.cleaned_data['email']}
        Phone: {form.cleaned_data['phone']}

        Message:
        {form.cleaned_data['message']}
        """,
            from_email='gereltjin.website.customer@gmail.com',
            to=['info@gereltjin.mn'],
            reply_to=[form.cleaned_data['email']],
        )

        email.send()    
        print("FORM SUBMITTED")
        return JsonResponse({'success': True})

    return JsonResponse({'errors': form.errors}, status=400)