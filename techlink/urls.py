from django.urls import path
from techlink.views import ProfessorSearchView
from techlink.views.home_view import home_page

app_name = 'techlink'

urlpatterns = [
    path('', home_page, name='home'),
    path('buscar/', ProfessorSearchView.as_view(), name='buscar'),
]
