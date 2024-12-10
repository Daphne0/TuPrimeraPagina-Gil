from django.db import models

# Create your models here.
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    disponibilidad = models.BooleanField(default=True)
    tamano = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Pedido de {self.cliente.nombre} - {self.fecha_pedido}"
