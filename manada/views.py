from django.shortcuts import render, redirect
from django.views.decorators import csrf
from .models import Comida, Cliente
from .forms import ComidaFrom, ClienteForm

# Create your views here.

def index(request):
    return render (request, 'index.html')

def quienSomos(request):
    return render (request, 'quienes-somos.html')

def contacto(request):
    return render (request, 'contacto.html')

def galeria(request):
    return render (request, 'galeria.html')

def registrarse(request):
    return render(request, 'registrarse.html')

def from_modcomida(request):
    return render(request, 'from_modcomida.html')

def form_crear_comida(request):
    return render(request, 'form_crear_comida.html')

def mostrar(request):
    comidas = Comida.objects.all()
    datos = {
        'comidas' : comidas
    }
    return render(request, 'mostrar.html', datos)

def from_modcomida(request, id):
    comida = Comida.objects.get(marca=id)
    datos = {
        'form': ComidaFrom(instance = comida)
    }
    if request.method=='POST':
        formulario = ComidaFrom(data=request.POST, instance = comida)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar')

    return render(request, 'from_modcomida.html', datos)

def clientes(request):
    clientes = Cliente.objects.all()
    datos = {
        'clientes' : clientes
    }
    return render(request, 'clientes.html', datos)


def form_del_comida(request,id):
    comida = Comida.objects.get(marca=id)
    comida.delete()
    return redirect('mostrar')

def form_comida(request):
    if request.method=='POST':
        comida_form = ComidaFrom(request.POST)
        if comida_form.is_valid():
            comida_form.save()
            return redirect ('mostrar')
    else:
        comida_form = ComidaFrom()
    return render(request, 'form_crear_comida.html', {'comida_form': comida_form})

def form_cliente(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ('clientes')
    else:
        cliente_form = ClienteForm()
    return render(request, 'form_cliente.html', {'cliente_form': cliente_form})

def form_modcliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect ('clientes')
        
    return render(request, 'form_modcliente.html', datos)

def form_del_cliente(request,id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('clientes')