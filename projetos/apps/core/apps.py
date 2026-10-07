from django.apps import AppConfig


class CoreConfig(AppConfig):
    # Define o tipo padrão de campo para as chaves primárias dos modelos.
    default_auto_field = 'django.db.models.BigAutoField'

    # Define o nome do aplicativo dentro da estrutura do projeto.
    name = 'core'

    # Define o nome que será exibido para o aplicativo no Django Admin.
    verbose_name = 'ModeloApp'