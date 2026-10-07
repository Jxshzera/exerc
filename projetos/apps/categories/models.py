from django.db import models


# Define o modelo de categorias utilizado pelo sistema.
class Category(models.Model):
    # Nome da categoria.
    name = models.CharField('Nome', max_length=50)

    # Descrição da categoria.
    description = models.TextField('Descricao', max_length=100)

    class Meta:
        # Define o nome do modelo no singular no Django Admin.
        verbose_name = 'Categoria'

        # Define o nome do modelo no plural no Django Admin.
        verbose_name_plural = 'Categorias'

        # Define a ordenação padrão das categorias pelo ID.
        ordering = ['id']

    # Define como cada categoria será representada em textos e no Admin.
    def __str__(self):
        return f'{self.id} - {self.name}'