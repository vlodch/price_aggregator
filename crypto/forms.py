# crypto/forms.py

from django import forms


class CryptoForm(forms.Form):
    amount = forms.DecimalField(label='Enter amount', max_digits=10, decimal_places=2)
