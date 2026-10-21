
from django.urls import path
from . import views

# Define o namespace das URLs deste aplicativo.
app_name = 'employees'

urlpatterns = [
    # Lista os funcionários cadastrados.
    path('listar/', views.list_employees, name='list_employees'),

    # Abre o formulário para cadastrar um funcionário.
    path('adicionar/', views.add_employee, name='add_employee'),

    # Abre o formulário para editar um funcionário existente.
    path('editar/<int:id_employee>/', views.edit_employee, name='edit_employee'),

    # Exclui um funcionário existente.
    path('excluir/<int:id_employee>/', views.delete_employee, name='delete_employee'),
]
