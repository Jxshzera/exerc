
from django.db import models

# Importa os modelos de produto e pedido.
from products.models import Product
from orders.models import Order


class Orderitem(models.Model):
    # Define a quantidade de unidades do produto no pedido.
    quantity = models.IntegerField('Quantidade', null=True, blank=True, default=0)

    # Armazena o preço unitário do produto no momento da compra.
    unit_price = models.FloatField('Preco unitario', null=True, blank=True, default=0.0)

    # Armazena o subtotal referente à quantidade do produto.
    subtotal = models.FloatField('Subtotal', null=True, blank=True, default=0.0)

    # Relaciona o item ao pedido e ao produto correspondente.
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')

    class Meta:
        # Define os nomes exibidos no painel administrativo.
        verbose_name = 'Item de pedido'
        verbose_name_plural = 'Itens de pedido'

        # Ordena os itens pelo identificador.
        ordering = ['id']

    # Retorna o identificador do item como representação textual.
    def __str__(self):
        return f'{self.id}'
