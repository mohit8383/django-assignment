from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('faq.urls')),  # Add this to serve the home view
    path('admin/', admin.site.urls),
    path('api/', include('faq.urls')),
]
