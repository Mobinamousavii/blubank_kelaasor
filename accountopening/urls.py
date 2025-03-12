from django.urls import path
from accountopening.views import account_opening

urlpatterns = [
    path('', account_opening)
]