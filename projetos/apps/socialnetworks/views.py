
from django.shortcuts import render, get_object_or_404, redirect

from .forms import SocialnetworkForm
from .models import Socialnetwork


# Create your views here.

# Cadastra uma nova rede social.
def add_socialnetwork(request):
    template_name = 'socialnetworks/add_socialnetwork.html'
    context = {}

    if request.method == 'POST':
        form = SocialnetworkForm(request.POST)

        if form.is_valid():
            # Salva a rede social após validar os dados.
            form.save()
            return redirect('socialnetworks:list_socialnetworks')
    else:
        # Apresenta um formulário vazio no primeiro acesso.
        form = SocialnetworkForm()

    # Mantém o formulário e eventuais erros de validação.
    context['form'] = form
    return render(request, template_name, context)


# Lista as redes sociais cadastradas.
def list_socialnetworks(request):
    template_name = 'socialnetworks/list_socialnetworks.html'

    # Recupera as redes sociais do banco de dados.
    socialnetworks = Socialnetwork.objects.all()

    context = {
        'socialnetworks': socialnetworks
    }
    return render(request, template_name, context)


# Edita uma rede social existente.
def edit_socialnetwork(request, id_socialnetwork):
    template_name = 'socialnetworks/add_socialnetwork.html'
    context = {}

    # Retorna a rede social ou uma página 404 se não existir.
    socialnetwork = get_object_or_404(
        Socialnetwork,
        id=id_socialnetwork
    )

    if request.method == 'POST':
        form = SocialnetworkForm(
            request.POST,
            instance=socialnetwork
        )

        if form.is_valid():
            form.save()
            return redirect('socialnetworks:list_socialnetworks')
    else:
        # Preenche o formulário com os dados atuais.
        form = SocialnetworkForm(instance=socialnetwork)

    context['form'] = form
    return render(request, template_name, context)


# Exclui uma rede social existente.
def delete_socialnetwork(request, id_socialnetwork):
    socialnetwork = get_object_or_404(
        Socialnetwork,
        id=id_socialnetwork
    )

    socialnetwork.delete()
    return redirect('socialnetworks:list_socialnetworks')
