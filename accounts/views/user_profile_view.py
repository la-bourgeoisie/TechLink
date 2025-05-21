from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from accounts.forms.user_form import CustomUserCreationForm

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/perfil_usuario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        form = CustomUserCreationForm(instance=usuario)
        context['usuario'] = usuario
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        usuario = request.user
        form = CustomUserCreationForm(request.POST, instance=usuario)

        if form.is_valid():
            form.save()
            return redirect('accounts:user_profile')

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)
