from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from accounts.forms.user_form import CustomPasswordChangeForm, CustomUserCreationForm, UserProfileUpdateForm
from accounts.forms.professor_form import ProfessorProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

class UserProfileEditView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user

        context['usuario'] = usuario
        context['profile_form'] = UserProfileUpdateForm(instance=usuario)
        context['password_form'] = CustomPasswordChangeForm(user=usuario)

        if usuario.tipo == 'professor':
            context['professor_form'] = ProfessorProfileForm(instance=usuario.professor_profile)

        return context


    def post(self, request, *args, **kwargs):
        usuario = request.user

        if 'submit_perfil' in request.POST:
            profile_form = UserProfileUpdateForm(request.POST, instance=usuario)
            if usuario.tipo == 'professor':
                professor_form = ProfessorProfileForm(request.POST, instance=usuario.professor_profile)
            else:
                professor_form = None

            if profile_form.is_valid() and (not professor_form or professor_form.is_valid()):
                profile_form.save()
                if professor_form:
                    professor_form.save()
                return redirect('accounts:user_profile')

            context = self.get_context_data()
            context['profile_form'] = profile_form
            if professor_form:
                context['professor_form'] = professor_form
            return self.render_to_response(context)

        elif 'submit_senha' in request.POST:
            password_form = PasswordChangeForm(user=usuario, data=request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                return redirect('accounts:user_profile')

            context = self.get_context_data()
            context['password_form'] = password_form
            return self.render_to_response(context)
        
        elif 'submit_professor' in request.POST:
            if usuario.tipo != 'professor':
                return redirect('accounts:user_profile')

            professor_form = ProfessorProfileForm(request.POST, instance=usuario.professor_profile)
            if professor_form.is_valid():
                professor_form.save()
                return redirect('accounts:user_profile')

            context = self.get_context_data()
            context['professor_form'] = professor_form
            return self.render_to_response(context)

        return redirect('accounts:user_profile')
