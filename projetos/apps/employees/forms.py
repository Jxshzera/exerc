
from django import forms
from .models import Employee

# Define o formulário baseado no modelo Employee.
class EmployeeForm(forms.ModelForm):

    class Meta:
        # Indica o modelo utilizado pelo formulário.
        model = Employee

        # Inclui todos os campos do modelo no formulário.
        exclude = ()
