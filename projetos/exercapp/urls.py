
"""
URL configuration for exercapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# Importa recursos necessários para disponibilizar arquivos de mídia
# durante o desenvolvimento do projeto.
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # URL de acesso ao painel administrativo do Django.
    path('admin/', admin.site.urls),

    # Encaminha a URL raiz do projeto para as URLs do aplicativo Core.
    path('', include('core.urls', namespace='core')),

    # Encaminha as URLs de categorias para o aplicativo Categories.
    path('categorias/', include('categories.urls', namespace='categories')),

    # Encaminha as URLs de produtos para o aplicativo Products.
    path('produtos/', include('products.urls', namespace='products')),

    # Encaminha as URLs de redes sociais para o aplicativo Socialnetworks.
    path('redessociais/', include('socialnetworks.urls', namespace='socialnetworks')),

    # Rotas do aplicativo de funcionários.
    path('funcionarios/', include('employees.urls', namespace='employees')),

    # Encaminha as URLs de clientes para o aplicativo Clients.
    path('clientes/', include('clients.urls', namespace='clients')),

    # Encaminha as URLs de pedidos para o aplicativo Orders.
    path('pedidos/', include('orders.urls', namespace='orders')),
]


# Configura o acesso aos arquivos enviados por upload durante o desenvolvimento.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
