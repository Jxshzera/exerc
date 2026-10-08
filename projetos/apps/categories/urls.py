from django.urls import path

from . import views


# Define o namespace das URLs do aplicativo Categories.
app_name = 'categories'


urlpatterns = [
    # Direciona a URL de cadastro para a view add_category.
    path('adicionar/', views.add_category, name='add_category'),

    # Direciona a URL de listagem para a view list_categories.
    path('listar/', views.list_categories, name='list_categories'),

    # Direciona a URL de edição para a view edit_category.
    # O <int:id_category> recebe o ID da categoria pela URL.
    path('editar/<int:id_category>/', views.edit_category, name='edit_category'),

    # Direciona a URL de exclusão para a view delete_category.
    # O <int:id_category> recebe o ID da categoria pela URL.
    path('excluir/<int:id_category>/', views.delete_category, name='delete_category'),
]