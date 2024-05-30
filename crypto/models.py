from django.db import models


class Currency(models.Model):
    symbol = models.CharField(max_length=50, unique=True)
    buy_from = models.CharField(max_length=100)
    sell_to = models.CharField(max_length=100)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.symbol

    class Meta:
        app_label = 'crypto'
