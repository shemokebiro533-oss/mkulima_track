from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Core URLs
    path('', include('core.urls')), 
    # Crops URLs
    path('crops/', include('crops.urls')),
]