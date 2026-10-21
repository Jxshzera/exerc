
from django.shortcuts import render, get_object_or_404, redirect

# Importa o formulário e os modelos necessários para gerenciar clientes.
from .forms import ClientForm
from .models import Client
from socialnetworks.models import Socialnetwork


# Create your views here.

# Exibe o formulário e salva um novo cliente quando enviado corretamente.
def add_client(request):
    template_name = 'clients/add_client.html'
    context = {}

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            # Salva primeiro o cliente para obter seu registro no banco.
            f = form.save(commit=False)
            f.save()

            # Salva os relacionamentos ManyToMany após salvar o cliente.
            form.save_m2m()

            return redirect('clients:list_clients')

    form = ClientForm()
    context['form'] = form
    return render(request, template_name, context)


# Lista os clientes e carrega antecipadamente suas redes sociais.
def list_clients(request):
    template_name = 'clients/list_clients.html'
    clients = Client.objects.prefetch_related('socialnetwork')

    context = {
        'clients': clients,
    }
    return render(request, template_name, context)


# Busca um cliente existente e permite editar seus dados.
def edit_client(request, id_client):
    template_name = 'clients/add_client.html'
    context = {}
    client = get_object_or_404(Client, id=id_client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients:list_clients')

    form = ClientForm(instance=client)
    context['form'] = form
    return render(request, template_name, context)


# Exclui o cliente identificado pelo ID e retorna à listagem.
def delete_client(request, id_client):
    client = get_object_or_404(Client, id=id_client)
    client.delete()
    return redirect('clients:list_clients')


# Realiza a busca de clientes pelo sobrenome informado no formulário.
def search_clients(request):
    template_name = 'clients/list_clients.html'

    # Recupera o sobrenome digitado pelo usuário.
    query = request.GET.get('query', '').strip()

    # Busca clientes cujo sobrenome contenha o texto informado.
    clients = Client.objects.filter(last_name__icontains=query)

    context = {
        'clients': clients,
    }

    return render(request, template_name, context)
