
from django import forms
from .models import Client


# Cria um formulário Django baseado no modelo Client.
class ClientForm(forms.ModelForm):

    class Meta:
        # Define qual modelo será utilizado para gerar os campos.
        model = Client

        # Mantém todos os campos do modelo disponíveis no formulário.
        exclude = ()
