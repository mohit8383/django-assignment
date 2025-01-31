from django.urls import path
from .views import get_faqs
from django.urls import path
from .views import get_faqs, home

urlpatterns = [
    path('', home, name='home'),
    path('faqs/', get_faqs, name='faq-list'),
]
