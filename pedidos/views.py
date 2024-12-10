from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ClienteForm, ProductoForm, PedidoForm
from .models import Cliente

# Vista para crear un cliente
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirigir a una página de inicio después de guardar
    else:
        form = ClienteForm()
    return render(request, 'pedidos/crear_cliente.html', {'form': form})

# Vista para crear un producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProductoForm()
    return render(request, 'pedidos/crear_producto.html', {'form': form})

# Vista para crear un pedido
def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/crear_pedido.html', {'form': form})

# Vista para buscar clientes
def buscar_cliente(request):
    resultados = None
    if 'q' in request.GET:
        query = request.GET['q']
        resultados = Cliente.objects.filter(nombre__icontains=query)
    return render(request, 'pedidos/buscar_cliente.html', {'resultados': resultados})

# Vista para la página de inicio
def index(request):
    return render(request, 'pedidos/inicio.html')