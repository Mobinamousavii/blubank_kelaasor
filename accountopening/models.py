from django.db import models
from services.models import  Transaction

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(null=True , blank=True)
    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=20)

class BankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_bankaccount")
    account_number = models.IntegerField(max_length=20)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)