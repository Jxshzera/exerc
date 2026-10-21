
from django.db import models

# Reutiliza os dados pessoais definidos no aplicativo persons.
from persons.models import Person

# Importa o modelo de redes sociais para criar o relacionamento com clientes.
from socialnetworks.models import Socialnetwork


# Create your models here.

# Define o modelo Cliente herdando os campos de Person.
# Assim, não precisamos declarar novamente nome, endereço, telefone e e-mail.
class Client(Person):

    # Permite selecionar o gênero do cliente por opções predefinidas.
    gender = models.CharField('Genero', max_length=1, choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ])

    # Permite associar várias redes sociais a um mesmo cliente.
    # Uma mesma rede social também pode estar associada a vários clientes.
    socialnetwork = models.ManyToManyField(
        Socialnetwork,
        verbose_name="Redes Socias"
    )

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    # Define como o objeto será representado como texto.
    def __str__(self):
        return super().first_name
        # Alternativa do professor: return super().__str__()
