from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from accounts.forms.professor_form import ProfessorProfileForm

class ProfessorProfileEditView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/professor_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        form = ProfessorProfileForm(instance=usuario)
        context['usuario'] = usuario
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        usuario = request.user
        form = ProfessorProfileForm(request.POST, instance=usuario)

        if form.is_valid():
            form.save()
            return redirect('accounts:user_profile')

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)
