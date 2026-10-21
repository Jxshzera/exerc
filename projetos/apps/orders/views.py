
from django.shortcuts import render, get_object_or_404, redirect

# Importa os modelos necessários para pedidos, itens, produtos,
# clientes e funcionários.
from orders.models import Order
from orderitems.models import Orderitem
from products.models import Product
from clients.models import Client
from employees.models import Employee


# Exibe todos os pedidos cadastrados.
def list_orders(request):
    template_name = 'orders/list_orders.html'

    # Carrega também os dados relacionados de cliente e funcionário.
    orders = Order.objects.select_related('client', 'employee').all()

    context = {
        'orders': orders,
    }

    return render(request, template_name, context)


# Exibe os produtos ativos disponíveis para compra.
def list_items_products(request):
    template_name = 'orders/list_items_products.html'

    # Filtra apenas os produtos ativos.
    products = Product.objects.filter(is_active=True)

    context = {
        'products': products,
    }

    return render(request, template_name, context)


# Exibe o carrinho de compras armazenado na sessão.
def cart(request):
    template_name = 'orders/cart.html'

    # Recupera o carrinho da sessão ou cria um carrinho vazio.
    cart_items = request.session.get('cart', {})

    # Soma os subtotais dos produtos para calcular o total.
    total = sum(item['subtotal'] for item in cart_items.values())

    context = {
        'cart': cart_items,
        'total': total,
    }

    return render(request, template_name, context)



# Adiciona um produto ao carrinho.
def add_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Recupera o carrinho e utiliza o ID do produto como chave.
    cart_items = request.session.get('cart', {})
    key = str(product.id)

    # Converte o preço Decimal para float para salvar na sessão JSON.
    price = float(product.price)

    # Se o produto já existe no carrinho, aumenta a quantidade.
    if key in cart_items:
        cart_items[key]['quantity'] += 1
        cart_items[key]['subtotal'] = (
            cart_items[key]['quantity'] * cart_items[key]['price']
        )
    else:
        # Caso contrário, adiciona o produto pela primeira vez.
        cart_items[key] = {
            'name': product.name,
            'price': price,
            'quantity': 1,
            'subtotal': price,
        }

    # Informa ao Django que a sessão foi alterada.
    request.session['cart'] = cart_items
    request.session.modified = True

    return redirect('orders:cart')


# Atualiza a quantidade de um produto no carrinho.
def edit_cart(request, product_id):
    if request.method == 'POST':
        cart_items = request.session.get('cart', {})
        key = str(product_id)

        if key in cart_items:
            try:
                quantity = int(request.POST.get('quantity', 1))
            except (TypeError, ValueError):
                quantity = 1

            # Quantidade zero ou negativa remove o produto.
            if quantity <= 0:
                del cart_items[key]
            else:
                cart_items[key]['quantity'] = quantity
                cart_items[key]['subtotal'] = (
                    quantity * cart_items[key]['price']
                )

            request.session['cart'] = cart_items
            request.session.modified = True

    return redirect('orders:cart')


# Remove um produto do carrinho.
def delete_cart(request, product_id):
    cart_items = request.session.get('cart', {})
    key = str(product_id)

    if key in cart_items:
        del cart_items[key]

    request.session['cart'] = cart_items
    request.session.modified = True

    return redirect('orders:cart')


# Finaliza a compra e registra o pedido no banco.
def checkout(request):
    template_name = 'orders/checkout.html'
    cart_items = request.session.get('cart', {})

    # Calcula o total atual do carrinho.
    total = sum(item['subtotal'] for item in cart_items.values())

    # Disponibiliza clientes e funcionários para o formulário.
    clients = Client.objects.all()
    employees = Employee.objects.all()

    if request.method == 'POST' and cart_items:
        client_id = request.POST.get('client_id')
        employee_id = request.POST.get('employee_id')
        payment_method = request.POST.get('payment_method')

        # Recupera os registros selecionados no formulário.
        client = get_object_or_404(Client, pk=client_id)
        employee = get_object_or_404(Employee, pk=employee_id)

        # Cria o pedido antes de registrar seus itens.
        order = Order.objects.create(
            client=client,
            employee=employee,
            payment_method=payment_method,
            status='Finalizado',
            total=0,
        )

        order_total = 0

        # Cria um item para cada produto presente no carrinho.
        for product_id, item in cart_items.items():
            product = get_object_or_404(Product, pk=product_id)
            quantity = int(item['quantity'])
            unit_price = float(item['price'])
            subtotal = quantity * unit_price

            Orderitem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                unit_price=unit_price,
                subtotal=subtotal,
            )

            order_total += subtotal

        # Atualiza o total final do pedido.
        order.total = order_total
        order.save()

        # Esvazia o carrinho depois de concluir a compra.
        request.session['cart'] = {}
        request.session.modified = True

        return redirect('orders:view_order', order_id=order.id)

    context = {
        'cart': cart_items,
        'total': total,
        'clients': clients,
        'employees': employees,
        'payment_methods': Order._meta.get_field(
            'payment_method'
        ).choices,
    }

    return render(request, template_name, context)


# Cancela um pedido, mantendo seu registro no banco.
def cancel_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if order.status != 'Cancelado':
        order.status = 'Cancelado'
        order.save()

    return redirect('orders:list_orders')


# Exibe os dados de um pedido e seus itens.
def view_order(request, order_id):
    template_name = 'orders/view_order.html'
    order = get_object_or_404(Order, pk=order_id)

    # Utiliza o relacionamento definido no modelo Orderitem.
    items = order.items.all()

    context = {
        'order': order,
        'items': items,
    }

    return render(request, template_name, context)
