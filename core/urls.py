"""
URL Configuration for Core app (Homepage, About, Contact)
"""
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('careers/', views.careers, name='careers'),
    path('services/', views.services, name='services'),

    # Dropdown submenu pages
    path('construction/', views.construction, name='construction'),
    path('glass-structure/', views.glass_structure, name='glass_structure'),
    path('windows-doors/', views.windows_doors, name='windows_doors'),
    path('rental/', views.rental, name='rental'),
    path('sports-hall/', views.sports_hall, name='sports_hall'),
]