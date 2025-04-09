from django.db import models

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

class Transaction(models.Model):
    account = models.ForeignKey(to=BankAccount, on_delete=models.CASCADE, related_name="origin_account")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)
    


