from django.http.response import HttpResponse
from services.models import Transaction
from accountopening.models import User, BankAccount
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import check_password

@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        
        username = data.get("username"),
        password = data.get("password"),

        user = User.objects.filter(name = username).first()

        if user is None:
            return HttpResponse("the user was not found.")
        
        if not check_password(password,user.password):
            return HttpResponse("your password is incorrect.")
        
        return HttpResponse(f"welcome {username}")

    return HttpResponse ("please enter your username and password")

@csrf_exempt
def sign_up(request):
    if request.method == "POST":
        data = json.loads(request.body)
        User.objects.create(
            username = data.get("username"),
            password = data.get("password"),
            phone = data.get("phone"),
            email = data.get("email"),
            national_id = data.get("national_id")
        )
        return HttpResponse("user created")
