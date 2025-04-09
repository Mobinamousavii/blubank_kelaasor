from django.urls import path
from accountopening.views import login,sign_up

urlpatterns = [
    path('login', login),
    path('sign-up', sign_up),
]