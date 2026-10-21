from django.db import models

# Importa o modelo Category para criar o relacionamento
# entre Produto e Categoria através de uma chave estrangeira.
from categories.models import Category

# Create your models here.

class Product(models.Model):
    # Nome do produto.
    name = models.CharField('Nome', max_length=50)

    # Descricao detalhada do produto.
    description = models.TextField('Descricao', max_length=200)

    # Data em que o produto foi fabricado.
    fabrication_date = models.DateField(
        'Data Fabricacao',
        auto_now=False,
        auto_now_add=False
    )

    # Define se o produto esta ativo.
    # O valor inicial sera False.
    is_active = models.BooleanField('Ativo', default=False)

    # Preco do produto.
    # max_digits = quantidade total de digitos.
    # decimal_places = quantidade de casas decimais.
    price = models.DecimalField(
        'Preço',
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # Imagem do produto.
    # Os arquivos serao armazenados dentro de media/photos.
    photo = models.ImageField('Foto', upload_to='photos')

    # Documento relacionado ao produto.
    # Os arquivos serao armazenados dentro de media/docs.
    doc = models.FileField('Documentos', upload_to='docs')

    # Relaciona cada produto com uma categoria.
    # Se a categoria for excluida, seus produtos relacionados
    # tambem serao excluidos por causa do CASCADE.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        # Nome exibido para um unico objeto.
        verbose_name = 'Produto'

        # Nome exibido para varios objetos.
        verbose_name_plural = 'Produtos'

        # Organiza os produtos pelo ID.
        ordering = ['id']

    def __str__(self):
        # Define como o produto sera representado como texto.
        return f'{self.name}'