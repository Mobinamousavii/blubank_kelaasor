from django.http.response import HttpResponse , JsonResponse
from loan.models import Loan , LoanBudget


def loan(request):
    return HttpResponse("which kind of loan do you want?")

def get_loan(request, loan_type):
    return HttpResponse(f"This page is for {loan_type}.")

def loan_accepeted(request, selected_loan):
    if request.method == "POST":
        try:
            loan = Loan.objects.get(id=selected_loan)
        except Loan.DoesNotExist:
            return HttpResponse("404")
        
    budget, created = LoanBudget.objects.get_or_create(id=1)

    if budget.total_budget >= loan.amount:

        budget.total_budget -= loan.amount
        budget.save()
        return("Loan approved")
    else:
        return('Bank does not have enough budget to accept this loan')
    

        