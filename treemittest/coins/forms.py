from django import forms


class BuyCoinsForm(forms.Form):
    quantity = forms.FloatField(label='Quantity', required=True)
    amount = forms.FloatField(label='Amount', required=True)
    coin_id = forms.IntegerField(widget=forms.HiddenInput())
