
from django.db import models

# Importa os modelos relacionados ao pedido.
from clients.models import Client
from employees.models import Employee


class Order(models.Model):
    # Registra automaticamente a data e a hora de criação do pedido.
    created_at = models.DateTimeField(auto_now_add=True)

    # Define as formas de pagamento disponíveis.
    payment_method = models.CharField(
        'Forma de pagamento',
        max_length=20,
        null=True,
        blank=True,
        default='Dinheiro',
        choices=[
            ('Dinheiro', 'Dinheiro'),
            ('Pix', 'Pix'),
            ('Cartao de Credito', 'Cartao de Credito'),
            ('Cartao de Debito', 'Cartao de Debito'),
        ]
    )

    # Define as situações possíveis do pedido.
    status = models.CharField(
        'Status',
        max_length=20,
        null=True,
        blank=True,
        default='Em andamento',
        choices=[
            ('Em andamento', 'Em andamento'),
            ('Finalizado', 'Finalizado'),
            ('Cancelado', 'Cancelado'),
        ]
    )

    # Armazena o valor total do pedido.
    total = models.FloatField('Preco Total', null=True, blank=True, default=0.0)

    # Relaciona o pedido ao cliente e ao funcionário responsável.
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        # Define os nomes exibidos no painel administrativo.
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

        # Ordena os pedidos pelo identificador.
        ordering = ['id']

    # Retorna o identificador do pedido como representação textual.
    def __str__(self):
        return f'{self.id}'
