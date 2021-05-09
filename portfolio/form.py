from django import forms
from .models import StockDB


class StockForm(forms.ModelForm):
    class Meta:
        model = StockDB
        fields = ['ticker']
