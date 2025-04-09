from django.urls import path
from services.views import services, get_service, transfer, recharge

urlpatterns = [
    path('', services),
    path('<str:service>', get_service),
    path('transfer',transfer ),
    path('recharge', recharge),
]