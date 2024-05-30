# profit_calculator/models.py

from django.db import models


class ProfitCurrency(models.Model):
    name = models.CharField(max_length=100)
    buy_platform = models.CharField(max_length=100)
    sell_platform = models.CharField(max_length=100)
    profit = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        app_label = 'profit_calculator'
