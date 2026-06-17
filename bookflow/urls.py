from django.contrib import admin
from django.urls import path, include  # Přidali jsme 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Všechny hlavní adresy posíláme do core/urls.py
]