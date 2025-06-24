from django.urls import path
from techlink.views import ProfessorSearchView

app_name = 'techlink'

urlpatterns = [
    path('buscar/', ProfessorSearchView.as_view(), name='buscar'),
]
