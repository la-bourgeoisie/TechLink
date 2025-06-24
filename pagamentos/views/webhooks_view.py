from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# VAI SER USADO QUANDO TIVERMOS O BANCO DE DADOS!!

@csrf_exempt # Webhooks não enviam token CSRF
def abacate_pay_webhook(request):
    """
    Recebe as notificações de pagamento do Abacate Pay.
    """
    if request.method != 'POST':
        return HttpResponse(status=405)

    try:
        payload = json.loads(request.body)
        event_type = payload.get('event') # Ex: 'charge.paid' (verificar na doc do Abacate Pay)

        # Verifique se o evento é de cobrança paga
        if event_type == 'charge.paid':
            charge_data = payload.get('data', {})
            charge_id = charge_data.get('id')

            if charge_id:
                # 1. Procure o pedido no seu banco de dados usando o charge_id
                # Ex: order = Order.objects.get(abacate_charge_id=charge_id)
                
                # 2. Atualize o status do pedido para "Pago"
                # Ex: order.status = 'PAID'
                #     order.save()
                
                # 3. Libere o produto/serviço para o cliente
                # (enviar email, dar acesso, etc.)
                
                print(f"Cobrança {charge_id} foi paga com sucesso!")
            
        # Responda ao Abacate Pay com status 200 para confirmar o recebimento
        return HttpResponse(status=200)

    except Exception as e:
        # Em caso de erro, logue e retorne um erro para que o Abacate Pay possa tentar novamente.
        print(f"Erro ao processar webhook do Abacate Pay: {e}")
        return JsonResponse({'error': 'Erro interno'}, status=400)