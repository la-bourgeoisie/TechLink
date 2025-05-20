from django.urls import path

app_name = 'agendamentos'

urlpatterns = [
    path('agendar/', 'agendamentos.views.agendar', name='agendar'),
    path('cancelar/', 'agendamentos.views.cancelar', name='cancelar'),
    path('historico/', 'agendamentos.views.historico', name='historico'),
    path('detalhes/<int:id>/', 'agendamentos.views.detalhes', name='detalhes'),
]