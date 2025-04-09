from django.contrib.admin import ModelAdmin
from accountopening.models import User,BankAccount
from django.contrib import admin

admin.site.register(User)
admin.site.register(BankAccount)
