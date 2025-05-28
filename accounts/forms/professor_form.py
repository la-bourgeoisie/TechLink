from django import forms
from accounts.models import PerfilProfessor, AreaConhecimento

class PerfilProfessorForm(forms.ModelForm):
    class Meta:
        model = PerfilProfessor
        fields = ['formacao', 'apresentacao', 'valor_hora', 'areas_conhecimento']
        widgets = {
            'areas_conhecimento': forms.CheckboxSelectMultiple,
        }
