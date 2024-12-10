from django import forms
from .models import Cliente, Producto, Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'direccion', 'email']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'tipo', 'disponibilidad', 'tamano']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'productos', 'estado', 'monto_total']
