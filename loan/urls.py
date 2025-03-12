from django.urls import path
from loan.views import loan, get_loan

urlpatterns = [
    path('',loan),
    path('<str:loan_type>', get_loan)
]