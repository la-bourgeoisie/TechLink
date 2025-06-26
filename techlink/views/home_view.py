from django.shortcuts import render
from accounts.models import ProfessorProfile 

def home_page(request):
    professores = ProfessorProfile.objects.select_related('usuario').all()[:6]

    context = {
        'professores': professores
    }

    return render(request, 'techlink/home.html', context)