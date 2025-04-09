from django.urls import path
from loan.views import loan, loan_accepeted

urlpatterns = [
    path('',loan),
    path('<str:loan_type>',loan_accepeted )
]