# profit_calculator/urls.py

from django.urls import path
from .views import aggregated_table

urlpatterns = [
    path('aggregated-table/', aggregated_table, name='aggregated_table'),
]
