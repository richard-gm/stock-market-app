from django import forms


# Own - user can enter tickers here
class TickerSymbolForm(forms.Form):
    ticker = forms.CharField(label="Ticker", max_length=5)
