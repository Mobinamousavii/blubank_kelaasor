from django.db import models
from services.models import Transaction
from accountopening.models import User, BankAccount

class Loan(models.Model):
    num_payments = models.PositiveIntegerField()
    amount = models.BigIntegerField()
    payment = models.BigIntegerField()
    loan_type = models.IntegerField(
        choices=[
            (1, "maskan"),
            (2, "ezdevaj"),
            (3, "daneshjou"),
            (4, "kar"),
        ]
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="loan_user")
    bank_account = models.ForeignKey(to=BankAccount, on_delete=models.CASCADE, related_name="BankAccount_loan")

class LoanBudget(models.Model):
    total_budget = models.DecimalField(max_digits=20, decimal_places=2)




