
from django.db import models

# Importa o modelo Person para reutilizar seus campos.
from persons.models import Person

# Create your models here.

# Define o modelo de funcionário herdando os dados de Person.
class Employee(Person):
    # Salário do funcionário.
    salary = models.FloatField(
        'Preço unitário',
        null=True,
        blank=True,
        default=0.0
    )

    # Cargo ocupado pelo funcionário.
    position = models.CharField('Nome', max_length=100)

    class Meta:
        # Define os nomes exibidos pelo Django.
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

        # Ordena os registros pelo ID.
        ordering = ['id']

    # Representa o funcionário pelo primeiro nome.
    def __str__(self):
        return super().first_name
        # Alternativa: return super().__str__()
