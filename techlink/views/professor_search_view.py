from django.views.generic import ListView
from accounts.models import ProfessorProfile
from django.db.models import Q

class ProfessorSearchView(ListView):
    model = ProfessorProfile
    template_name = 'techlink/home.html'
    context_object_name = 'professores'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return ProfessorProfile.objects.filter(
            Q(usuario__nome__icontains=query) |
            Q(areas_conhecimento__icontains=query)
        )
