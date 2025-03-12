from django.urls import path
from services.views import services, get_service

urlpatterns = [
    path('', services),
    path('<str:service>', get_service),
]