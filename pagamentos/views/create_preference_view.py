import json
import requests
import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY

@csrf_exempt
def create_payment(request):
    """
    Cria uma intenção de pagamento para Cartão (Stripe) ou uma cobrança Pix (Abacate Pay).
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)

    try:
        data = json.loads(request.body)
        payment_method = data.get('payment_method')
        amount_in_cents = 4600  # R$ 46,00 em centavos

        if payment_method == 'card':
            intent = stripe.PaymentIntent.create(
                amount=amount_in_cents,
                currency="brl",
                payment_method_types=["card"],
                metadata={"order_id": "sessao_fernando_ribeiro_001"}
            )
            return JsonResponse({"clientSecret": intent.client_secret})

        elif payment_method == 'pix':     
            pix_creation_url = "https://api.abacatepay.com/v1/pixQrCode/create"

            payload = {
                "amount": amount_in_cents
            }

            headers = {
                "Authorization": f"Bearer {settings.ABACATE_PAY_API_KEY}",
                "Content-Type": "application/json"
            }

            response = requests.post(pix_creation_url, json=payload, headers=headers)
            response_data = response.json()
            
            print("DEBUG: Resposta da API Abacate Pay ->", response_data)
            
            if response.status_code >= 400:
                return JsonResponse({'error': response_data}, status=400)

            data_object = response_data.get('data', {})

            pix_data = {
                "qr_code_image": data_object.get("brCodeBase64"), 
                "qr_code_text": data_object.get("brCode"),       
                "charge_id": data_object.get("id")              
            }
            
            if not pix_data["qr_code_image"] or not pix_data["qr_code_text"]:
                return JsonResponse({'error': 'A resposta da API não continha os dados do QR Code. Verifique o console do Django.'}, status=500)
            
            return JsonResponse(pix_data)

        else:
            return JsonResponse({'error': 'Método de pagamento inválido'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
