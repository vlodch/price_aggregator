# crypto/admin.py

from django.contrib import admin
from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'buy_from', 'sell_to', 'buy_price')