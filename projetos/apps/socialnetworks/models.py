
from django.db import models


# Create your models here.

# Define o modelo responsável pelo cadastro de redes sociais.
class Socialnetwork(models.Model):
    # Nome da rede social.
    name = models.CharField('Nome', max_length=50)

    # Tipo de conteúdo publicado na rede social.
    content_type = models.TextField('Tipo de conteúdo', max_length=100)

    # Endereço da rede social na internet.
    url = models.CharField('URL da Rede Social', max_length=200)

    class Meta:
        # Define os nomes exibidos pelo Django.
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'

        # Ordena os registros pelo ID.
        ordering = ['id']

    # Define como a rede social será representada em texto.
    def __str__(self):
        return f'{self.name}'
