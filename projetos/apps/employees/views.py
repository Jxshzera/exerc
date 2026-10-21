
from django.shortcuts import render, get_object_or_404, redirect

from .forms import EmployeeForm
from .models import Employee

# Create your views here.

# Cadastra um novo funcionário.
def add_employee(request):
    template_name = 'employees/add_employee.html'
    context = {}

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Salva os dados do funcionário após validar o formulário.
            employee = form.save(commit=False)
            employee.save()
            form.save_m2m()
            return redirect('employees:list_employees')
    else:
        # Exibe um formulário vazio no primeiro acesso.
        form = EmployeeForm()

    # Mantém o formulário e eventuais erros de validação.
    context['form'] = form
    return render(request, template_name, context)


# Lista os funcionários cadastrados.
def list_employees(request):
    template_name = 'employees/list_employees.html'

    # Recupera os funcionários cadastrados no banco de dados.
    employees = Employee.objects.all()

    context = {
        'employees': employees,
    }
    return render(request, template_name, context)


# Edita um funcionário existente.
def edit_employee(request, id_employee):
    template_name = 'employees/add_employee.html'
    context = {}

    # Busca o funcionário ou retorna erro 404 se não existir.
    employee = get_object_or_404(Employee, id=id_employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees:list_employees')
    else:
        # Preenche o formulário com os dados atuais.
        form = EmployeeForm(instance=employee)

    context['form'] = form
    return render(request, template_name, context)


# Exclui um funcionário existente.
def delete_employee(request, id_employee):
    employee = get_object_or_404(Employee, id=id_employee)
    employee.delete()
    return redirect('employees:list_employees')
