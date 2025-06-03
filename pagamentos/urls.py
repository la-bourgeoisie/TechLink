from django.urls import path
from pagamentos.views import (
    CheckoutView
)

app_name = 'pagamentos'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='pagamentos'),
]

