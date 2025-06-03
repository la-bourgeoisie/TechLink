from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from pagamentos.forms.cartao_checkout_form import CustomCheckoutForm

class CheckoutView(FormView):
    template_name = 'pagamentos/checkout.html'
    form_class = CustomCheckoutForm
    success_url = reverse_lazy('pagamento:sucesso')

