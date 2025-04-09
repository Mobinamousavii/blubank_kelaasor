from django.http.response import HttpResponse
from services.models import User, Transaction, BankAccount
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import check_password

def services(request):
    return HttpResponse("choose your service")

def get_service(request, service):
    return HttpResponse(f"This page is for {service}.")

