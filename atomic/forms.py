from django import forms


class Payment(forms.Form):
    payor = forms.CharField(max_length=30, label=('payor'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    payee = forms.CharField(max_length=30, label=('payee'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    amount = forms.CharField(max_length=30, label=('amount'), widget=forms.TextInput(attrs={'class': 'form-control'}))
