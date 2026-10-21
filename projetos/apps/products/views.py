from django.shortcuts import render, get_object_or_404, redirect

# Importa o formulário utilizado para cadastrar e editar produtos.
from .forms import ProductForm

# Importa o modelo Product para consultar, cadastrar,
# editar e excluir produtos.
from .models import Product



def add_product(request):
    # Define o template utilizado para cadastro de produtos.
    template_name = 'products/add_product.html'

    # Cria o contexto que será enviado para o template.
    context = {}

    # Verifica se o formulário foi enviado.
    if request.method == 'POST':
        # Recebe os dados e os arquivos enviados pelo usuário.
        form = ProductForm(request.POST, request.FILES)

        # Verifica se todos os campos passaram pela validação.
        if form.is_valid():
            # Salva o produto no banco de dados.
            product = form.save()

            # Redireciona para a lista após salvar com sucesso.
            return redirect('products:list_products')
    else:
        # Em um acesso normal, apresenta um formulário vazio.
        form = ProductForm()

    # Mantém os dados e erros do formulário quando inválido.
    context['form'] = form

    # Exibe o formulário de cadastro.
    return render(request, template_name, context)


    # Cria um formulario vazio quando a pagina e acessada pela primeira vez.
    form = ProductForm()

    # Envia o formulario para o template.
    context['form'] = form

    return render(request, template_name, context)


def list_products(request):
    # Define o template utilizado para listar os produtos.
    template_name = 'products/list_products.html'

    # Busca os produtos cadastrados no banco de dados.
    products = Product.objects.filter()

    context = {
        'products': products
    }

    return render(request, template_name, context)


def edit_product(request, id_product):
    # O mesmo template utilizado no cadastro tambem sera utilizado
    # para editar um produto.
    template_name = 'products/add_product.html'
    context = {}

    # Procura o produto pelo ID.
    # Caso ele nao exista, o Django retorna uma pagina 404.
    product = get_object_or_404(Product, id=id_product)

    # Verifica se o formulario de edicao foi enviado.
    if request.method == 'POST':
        # instance=product informa qual produto sera atualizado.
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            # Salva as alteracoes do produto.
            form.save()

            # Volta para a lista de produtos.
            return redirect('products:list_products')

    # Preenche o formulario com os dados atuais do produto.
    form = ProductForm(instance=product)

    context['form'] = form

    return render(request, template_name, context)


def delete_product(request, id_product):
    # Procura o produto pelo ID.
    product = Product.objects.get(id=id_product)

    # Exclui o produto do banco de dados.
    product.delete()

    # Volta para a lista de produtos.
    return redirect('products:list_products')