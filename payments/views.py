
from app.settings import PAYSTACK_SECRET_KEY, PAYSTACK_PUBLIC_KEY

from django.views.generic import CreateView
from .forms import PaymentForms
from .models import Payments

# Create your views here.

class MakePaymentView(CreateView):
    model = Payments
    form_class = PaymentForms
    template_name = 'payments.html'
     

    def get_context_data(self, **kwargs):
        paystack_public_key = PAYSTACK_PUBLIC_KEY
        context = super().get_context_data(**kwargs)
        context.update({'paystack_public_key': paystack_public_key})
        return context




        
