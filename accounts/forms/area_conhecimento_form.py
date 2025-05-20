from django import forms
from accounts.models import AreaConhecimento

class AreaConhecimentoForm(forms.ModelForm):
    class Meta:
        model = AreaConhecimento
        fields = ['nome']
