from django.http.response import HttpResponse , JsonResponse
from services.models import User, Transaction, BankAccount
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import check_password

def services(request):
    return HttpResponse("choose your service")

def get_service(request, service):
    return HttpResponse(f"This page is for {service}.")

def transfer(request, sender_account_id, destination_account_id, amount):
    if request.method == "POST":
        try:
            sender_account = BankAccount.objects.get(id=sender_account_id)
            receiver_account = BankAccount.objects.get(id=destination_account_id)
        except BankAccount.DoesNotExist:
                return HttpResponse("not valid")
    
    if sender_account.balance < amount:
        return HttpResponse('Insufficient balance')

    sender_account.balance -= amount
    receiver_account.balance += amount
    sender_account.save()
    receiver_account.save()

    
    Transaction.objects.create(
        transaction_type='transfer',
        account=sender_account,
        amount=amount,
        destination_account=receiver_account
    )

    return JsonResponse('Transfer completed successfully')

def recharge(request, account_id, amount):
    if request.method == "POST":
        try:
            account = BankAccount.objects.get(id=account_id)
        except BankAccount.DoesNotExist:
            return HttpResponse("not valid")
        account.balance += amount
        account.save()

        Transaction.objects.create(
            transaction_type='charge',
            account=account,
            amount=amount
        )

    return HttpResponse('Account charged successfully')


