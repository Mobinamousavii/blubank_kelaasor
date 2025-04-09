from django.contrib.admin import ModelAdmin
from services.models import Transaction
from django.contrib import admin

admin.site.register(Transaction)
