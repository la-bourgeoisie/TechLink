from django import forms
from accounts.models import PerfilAluno

class PerfilAlunoForm(forms.ModelForm):
    class Meta:
        model = PerfilAluno
        fields = []
