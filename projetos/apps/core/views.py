from django.shortcuts import render


# Renderiza a página inicial do aplicativo Core.
def home(request):
    # Define o template HTML que será utilizado pela página inicial.
    template_name = 'core/home.html'

    # Define o contexto que será enviado para o template.
    context = {}

    # Renderiza o template e retorna a resposta para o navegador.
    return render(request, template_name, context)