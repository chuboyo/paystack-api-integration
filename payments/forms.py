from django import forms 

from .models import Payments

class PaymentForms(forms.ModelForm):
    class Meta:
        model = Payments
        fields = '__all__'
        widgets = {'ref': forms.HiddenInput()}