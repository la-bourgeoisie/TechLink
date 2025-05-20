from django.urls import path

app_name = 'pagamentos'

urlpatterns = [
    path('pagamento/<int:id>/', 'pagamentos.views.pagamento', name='pagamento'),
    path('pagamentos/', 'pagamentos.views.pagamentos', name='pagamentos'),
    path('pagamento/<int:id>/editar/', 'pagamentos.views.editar_pagamento', name='editar_pagamento'),
    path('pagamento/<int:id>/deletar/', 'pagamentos.views.deletar_pagamento', name='deletar_pagamento'),
]