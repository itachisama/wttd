# coding: utf-8
from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription


def CPFValidator(value):
    if not value.isdigit():
        raise ValidationError(_(u'CPF deve conter apenas números'))
    if len(value) != 11:
        raise ValidationError(_(u'CPF deve ter 11 números'))


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        exclude = ('paid')
        fields = ('name', 'cpf', 'email', 'phone')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)

        self.fields['cpf'].validators.append(CPFValidator)
