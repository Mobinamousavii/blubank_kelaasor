from django.db import models
from accountopening.models import User, BankAccount
class Transaction(models.Model):
    account = models.ForeignKey(to=BankAccount, on_delete=models.CASCADE, related_name="origin_account")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)
    


