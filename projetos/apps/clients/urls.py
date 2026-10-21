
from django.urls import path
from . import views

# Define o namespace usado para identificar as URLs de clientes.
app_name = 'clients'

urlpatterns = [
    # Exibe a lista de clientes cadastrados.
    path('listar/', views.list_clients, name='list_clients'),

    # Abre o formulário de cadastro.
    path('adicionar/', views.add_client, name='add_client'),

    # Abre o formulário para editar um cliente pelo ID.
    path('editar/<int:id_client>/', views.edit_client, name='edit_client'),

    # Exclui um cliente pelo ID.
    path('excluir/<int:id_client>/', views.delete_client, name='delete_client'),

    # Exclui um cliente pelo ID.
    path('excluir/<int:id_client>/', views.delete_client, name='delete_client'),

    # Pesquisa clientes pelo sobrenome informado.
    path('buscar/', views.search_clients, name='search_clients'),

]
