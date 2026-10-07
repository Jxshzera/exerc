from django import forms

from .models import Category


# Define o formulário baseado no modelo Category.
class CategoryForm(forms.ModelForm):

    class Meta:
        # Define o modelo utilizado pelo formulário.
        model = Category

        # Inclui todos os campos do modelo no formulário.
        exclude = ()