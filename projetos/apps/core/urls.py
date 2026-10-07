from django.urls import path
from . import views

# Define o nome do aplicativo para utilização das URLs com namespace.
app_name = 'core'


urlpatterns = [
    # Direciona a URL raiz do Core para a função home.
    path('', views.home, name='home'),
]