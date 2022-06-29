from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import AddEmployees


# Create your views here.

def index(request):
    employess = AddEmployees.objects.all().order_by('id')
    paginator = Paginator(employess, per_page=2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj' : page_obj})

def add_employees(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']

        employes = AddEmployees.objects.create(name=name, email=email, address=address, phone=phone)
        employes.save()

        return redirect('/')
    else:
        return redirect('/')

def edit_employee(request):
    if request.method == 'POST':
        emp_id = request.POST['emp_id']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        employee = AddEmployees.objects.get(pk=emp_id)
        employee.name = name
        employee.email = email
        employee.address = address
        employee.phone = phone
        employee.save()
        return redirect('/')
    else:
        return redirect('/')

def delete_employee(request):
    if request.method == 'POST':
        emp_id = request.POST['emp_id']
        employee = AddEmployees.objects.filter(id= emp_id)
        employee.delete()
        return redirect('/')
    else:
        return redirect('/')
    
