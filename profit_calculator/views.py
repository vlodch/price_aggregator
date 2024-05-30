# profit_calculator/views.py

from django.shortcuts import render
from .models import Currency


def aggregated_table(request):
    currencies = Currency.objects.all()
    context = {'currencies': currencies}
    return render(request, 'aggregated_data.html', context)
