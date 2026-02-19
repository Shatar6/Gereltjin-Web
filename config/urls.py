"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', RedirectView.as_view(url='/mn/', permanent=False)),  # Redirect root to Mongolian version
]


# Add language prefix to all URLs (for Mongolian/English switching)
urlpatterns += i18n_patterns(
    path('', include('core.urls')),  # Home page and main content
    path('accounts/', include('accounts.urls')),  # User accounts
    path('orders/', include('orders.urls')),  # Order system
    path('services/', include('services.urls')),  # Services pages
    path('portfolio/', include('portfolio.urls')),  # Portfolio/Projects
)

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Customize admin site
admin.site.site_header = "Gereltjin LLC Admin"
admin.site.site_title = "Gereltjin Admin Portal"
admin.site.index_title = "Welcome to Gereltjin LLC Management"
