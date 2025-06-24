from django.conf import settings
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from pagamentos.forms.cartao_checkout_form import CustomCheckoutForm
from django.core.exceptions import ImproperlyConfigured

class CheckoutView(FormView):
    template_name = 'pagamentos/checkout.html'
    form_class = CustomCheckoutForm
    success_url = reverse_lazy('pagamento:sucesso')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
   
        if not hasattr(settings, 'STRIPE_PUBLISHABLE_KEY') or not settings.STRIPE_PUBLISHABLE_KEY:
            raise ImproperlyConfigured(
                "A chave STRIPE_PUBLISHABLE_KEY não foi encontrada ou está vazia no seu arquivo settings.py. "
            )
        
        context['STRIPE_PUBLISHABLE_KEY'] = settings.STRIPE_PUBLISHABLE_KEY
        
        return context
