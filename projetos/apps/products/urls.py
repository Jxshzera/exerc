from django.urls import path

# Importa as views do aplicativo Products.
# As funcoes de views serao associadas as URLs abaixo.
from . import views


# Namespace utilizado para identificar as URLs do aplicativo Products.
app_name = 'products'


urlpatterns = [
    # Lista todos os produtos cadastrados.
    path('listar/', views.list_products, name='list_products'),

    # Abre o formulario para adicionar um novo produto.
    path('adicionar/', views.add_product, name='add_product'),

    # Edita um produto utilizando o ID recebido pela URL.
    path('editar/<int:id_product>/', views.edit_product, name='edit_product'),

    # Exclui um produto utilizando o ID recebido pela URL.
    path('excluir/<int:id_product>/', views.delete_product, name='delete_product'),
]