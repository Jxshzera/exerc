
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CategoryForm
from .models import Category


# Exibe o formulário e realiza o cadastro de uma nova categoria.
def add_category(request):
    # Define o template utilizado pela página de cadastro.
    template_name = 'categories/add_category.html'

    # Define o contexto que será enviado para o template.
    context = {}

    # Verifica se o formulário foi enviado através do método POST.
    if request.method == 'POST':
        # Cria o formulário utilizando os dados enviados pelo usuário.
        form = CategoryForm(request.POST)

        # Verifica se os dados preenchidos são válidos.
        if form.is_valid():
            # Cria o objeto sem salvá-lo imediatamente no banco.
            f = form.save(commit=False)

            # Salva a categoria no banco de dados.
            f.save()

            # Salva possíveis relacionamentos ManyToMany do formulário.
            form.save_m2m()

            # Após salvar, redireciona para a lista de categorias.
            return redirect('categories:list_categories')

    # Cria um formulário vazio quando a página é acessada pela primeira vez.
    form = CategoryForm()

    # Adiciona o formulário ao contexto enviado para o template.
    context['form'] = form

    # Renderiza o template e retorna a resposta para o navegador.
    return render(request, template_name, context)


# Lista todas as categorias cadastradas no sistema.
def list_categories(request):
    # Define o template utilizado pela página de listagem.
    template_name = 'categories/list_categories.html'

    # Busca todas as categorias cadastradas no banco de dados.
    categories = Category.objects.filter()

    # Define os dados que serão enviados para o template.
    context = {
        'categories': categories
    }

    # Renderiza a página de listagem de categorias.
    return render(request, template_name, context)


# Exibe o formulário e realiza a edição de uma categoria existente.
def edit_category(request, id_category):
    # Define o mesmo template utilizado no cadastro de categorias.
    template_name = 'categories/add_category.html'

    # Define o contexto que será enviado para o template.
    context = {}

    # Busca a categoria pelo ID.
    # Caso ela não exista, o Django retorna uma página 404.
    category = get_object_or_404(Category, id=id_category)

    # Verifica se o formulário foi enviado através do método POST.
    if request.method == 'POST':
        # Cria o formulário com os dados enviados e vinculado à categoria existente.
        form = CategoryForm(request.POST, instance=category)

        # Verifica se os dados preenchidos são válidos.
        if form.is_valid():
            # Salva as alterações realizadas na categoria.
            form.save()

            # Após salvar, redireciona para a lista de categorias.
            return redirect('categories:list_categories')

    # Cria o formulário preenchido com os dados atuais da categoria.
    form = CategoryForm(instance=category)

    # Adiciona o formulário ao contexto enviado para o template.
    context['form'] = form

    # Renderiza o formulário de edição.
    return render(request, template_name, context)


# Exclui uma categoria existente pelo seu ID.
def delete_category(request, id_category):
    # Busca a categoria pelo ID informado na URL.
    category = Category.objects.get(id=id_category)

    # Exclui a categoria do banco de dados.
    category.delete()

    # Após excluir, redireciona para a lista de categorias.
    return redirect('categories:list_categories')
