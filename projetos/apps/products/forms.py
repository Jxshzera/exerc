
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ()

        # Define o formato de data utilizado no formulário.
        widgets = {
            'fabrication_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date'}
            ),
        }

    # Aceita a data enviada pelo campo HTML do tipo date.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fabrication_date'].input_formats = [
            '%Y-%m-%d',
            '%d/%m/%Y',
        ]
