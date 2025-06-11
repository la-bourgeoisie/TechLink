from django.urls import path
from .views import ProfessorBuscaView

app_name = 'techlink'

urlpatterns = [
    path('buscar/', ProfessorBuscaView.as_view(), name='buscar_professor'),
]
