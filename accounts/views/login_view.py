from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from accounts.forms import CustomAuthenticationForm

class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('accounts:user_profile')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            primeira_vez = user.last_login is None

            login(self.request, user)

            if primeira_vez:
                return redirect('accounts:user_profile')  # nome da URL para o primeiro login

            return super().form_valid(form)
        else:
            form.add_error(None, "Email ou senha inválidos.")
            return self.form_invalid(form)
