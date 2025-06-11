from django.views.generic import ListView
from .models import PerfilProfessor

class BuscarProfessorView(ListView):
    model = PerfilProfessor
    template_name = 'buscar_professores.html'
    context_object_name = 'professores'

    def get_queryset(self):
        queryset = super().get_queryset()
        termo = self.request.GET.get('q')

        if termo:
            queryset = queryset.filter(apresentacao__icontains=termo)

        return queryset
