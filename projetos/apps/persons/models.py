
from django.db import models

# Create your models here.

# Define o modelo responsável pelo cadastro de pessoas.
class Person(models.Model):
    # Nome e sobrenome da pessoa.
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100)

    # Endereço e telefone para contato.
    address = models.CharField('Endereço', max_length=200)
    phone = models.CharField('Telefone celular', max_length=20)

    # E-mail obrigatório da pessoa.
    email = models.EmailField('E-mail', null=False, blank=False)

    class Meta:
        # Define os nomes exibidos pelo Django.
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

        # Ordena os registros pelo ID.
        ordering = ['id']

    # Define como a pessoa será representada em texto.
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
