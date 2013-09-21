# coding: utf-8
from django import forms
from eventex.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ('name', 'cpf', 'email', 'phone')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
