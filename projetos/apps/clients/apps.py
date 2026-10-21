
from django.apps import AppConfig


# Define as configurações iniciais do aplicativo Clients.
class ClientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clients'

    # Nome que será exibido para identificar o aplicativo no Django Admin.
    verbose_name = 'Clientes'
