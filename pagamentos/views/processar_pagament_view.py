import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import mercadopago

@csrf_exempt  # porque estamos recebendo POST via fetch JS
def processar_pagamento(request):
    if request.method == "POST":
        sdk = mercadopago.SDK("TEST-6401297577337636-060610-fe751cba6f24a4e7a21436d5d229d112-164248434")

        data = json.loads(request.body)

        payment_data = {
            "transaction_amount": float(data.get("transactionAmount", 0)),
            "token": data.get("token"),
            "description": data.get("description"),
            "installments": int(data.get("installments", 1)),
            "payment_method_id": data.get("paymentMethodId"),
            "payer": data.get("payer"),
        }

        payment_response = sdk.payment().create(payment_data)
        payment = payment_response["response"]

        if payment_response["status"] == 201:
            return JsonResponse({"status": "success", "payment_id": payment.get("id")})
        else:
            return JsonResponse({"status": "error", "message": payment.get("message", "Erro no pagamento")})

    return JsonResponse({"status": "error", "message": "Método inválido"}, status=405)
