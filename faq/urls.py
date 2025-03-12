from django.urls import path
from faq.views import faq

urlpatterns = [
    path('', faq)
]