# crypto/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aggregated_data/', views.aggregated_data_view, name='aggregated_data'),
    # Comment out the calculate_profit URL pattern if it's not needed
    # path('calculate_profit/<str:symbol>/<str:amount>/', views.calculate_profit, name='calculate_profit'),
]
