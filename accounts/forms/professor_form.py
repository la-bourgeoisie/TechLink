from django import forms
from accounts.models import ProfessorProfile

class ProfessorProfileForm(forms.ModelForm):
    class Meta:
        model = ProfessorProfile
        fields = ['formacao', 'apresentacao', 'valor_hora', 'areas_conhecimento']
        widgets = {
            'formacao': forms.Textarea(attrs={'class': 'form-control'}),
            'apresentacao': forms.Textarea(attrs={'class': 'form-control'}),
            'valor_hora': forms.NumberInput(attrs={'class': 'form-control'}),
            'areas_conhecimento': forms.Textarea(attrs={'class': 'form-control'}),
        }
