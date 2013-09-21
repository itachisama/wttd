# coding: utf-8
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def setUp(self):
        self.form = SubscriptionForm()

    def test_has_fields(self):
        'Form must have 4 fields.'
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'],
                              self.form.fields)

    def test_has_form(self):
        'Context must have the subscription form.'
        self.assertIsInstance(self.form, SubscriptionForm)
