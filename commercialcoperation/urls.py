from django.urls import path
from commercialcoperation.views import commercial_coperation

urlpatterns = [
    path('', commercial_coperation)
]