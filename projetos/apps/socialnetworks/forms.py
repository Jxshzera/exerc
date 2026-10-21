
from django import forms
from .models import Socialnetwork


# Define o formulário baseado no modelo Socialnetwork.
class SocialnetworkForm(forms.ModelForm):

    class Meta:
        # Indica qual modelo será utilizado.
        model = Socialnetwork

        # Inclui todos os campos do modelo no formulário.
        exclude = ()
