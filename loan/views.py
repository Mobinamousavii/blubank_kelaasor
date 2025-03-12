from django.http.response import HttpResponse

def loan(request):
    return HttpResponse("which kind of loan do you want?")

def get_loan(request, loan_type):
    return HttpResponse(f"This page is for {loan_type}.")
