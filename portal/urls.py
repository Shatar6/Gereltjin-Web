"""
URL Configuration for Portal app (Order Management)
"""
from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<int:pk>/', views.order_detail, name='order_detail'),

    # CUSTOMER URLS
    path('request/', views.create_order, name='create_order'),
    path('my-quotes/', views.customer_quotes, name='customer_quotes'),
    path('profile/', views.customer_profile, name='customer_profile'),
    
    # EMPLOYEE PORTAL URLS
    path('portal_login/', views.portal_login, name='portal_login'),
    path('dashboard/', views.portal_dashboard, name='portal_dashboard'),
    path('apartments/', views.portal_apartments, name='portal_apartments'),
    path('machines/', views.portal_machines, name='portal_machines'),
    path('vehicles/', views.portal_vehicles, name='portal_vehicles'),
    path('quotations/', views.portal_quotations, name='portal_quotations'),

    path('apartments/add/', views.portal_apartment_add, name='apartments_add'),
    path('machines/add-maintenance/', views.portal_machine_add_maintenance, name='machines_add_maintenance'),
    path('vehicles/add-service/', views.portal_vehicle_add_service, name='vehicles_add_service'),
]