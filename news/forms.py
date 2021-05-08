from django import forms


# Own - user can enter tickers to get news
class TickerSymbolNewsForm(forms.Form):
    ticker = forms.CharField(label="Ticker", max_length=5)
