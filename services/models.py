from django.db import models
from accountopening.models import User, BankAccount
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('transfer', 'Transfer'),
        ('charge', 'Charge'),
        ('bill', 'Bill Payment'),
    )

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    account = models.ForeignKey(to=BankAccount, on_delete=models.CASCADE, related_name="origin_account")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)
    destination_account = models.ForeignKey(to=BankAccount, null=True, blank=True, on_delete=models.SET_NULL, related_name="destination_account")
    


