from django import forms

class CustomCheckoutForm(forms.Form):
    name = forms.CharField(label="Nome",
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 mb-5 outline-none',
            'placeholder': 'Nome no Cartão'
        })
    )
    number = forms.CharField(label="Número", 
        widget=forms.TextInput(attrs={
            'id': 'card-number',
            'class': 'w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 mb-7 outline-none',
            'maxlength': '19',
            'placeholder': 'Número do Cartão'
        })
    )
    expiration_date = forms.CharField(label="Data de Validade", 
        widget=forms.TextInput(attrs={
            'id': 'expiration-date',
            'class': 'w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 mb-7 outline-none',
            'maxlength': '5',
            'placeholder': 'MM / AA'
        })
    )
    cvc = forms.CharField(label="CVC", 
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 mb-7 outline-none',
            'maxlength': '3',
            'placeholder': 'Código de Segurança'
        })
    )