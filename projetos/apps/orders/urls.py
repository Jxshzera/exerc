
from django.urls import path
from . import views

# Define o namespace usado para identificar as URLs de pedidos.
app_name = 'orders'

urlpatterns = [
    # Exibe os produtos disponíveis para compra.
    path('itens/', views.list_items_products, name='list_items_products'),

    # Exibe e manipula o carrinho de compras.
    path('carrinho/', views.cart, name='cart'),
    path('carrinho/adicionar/<int:product_id>/', views.add_cart, name='add_cart'),
    path('carrinho/editar/<int:product_id>/', views.edit_cart, name='edit_cart'),
    path('carrinho/excluir/<int:product_id>/', views.delete_cart, name='delete_cart'),

    # Finaliza a compra.
    path('checkout/', views.checkout, name='checkout'),

    # Lista, visualiza e cancela pedidos.
    path('listar/', views.list_orders, name='list_orders'),
    path('itens/<int:order_id>/', views.view_order, name='view_order'),
    path('itens/<int:order_id>/cancelar/', views.cancel_order, name='cancel_order'),
]
