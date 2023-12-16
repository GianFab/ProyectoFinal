import random
from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models

class Producto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    oferta = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    def precio_oferta(self):
        if self.oferta:
            factor_descuento = Decimal(random.uniform(1.25, 2))

            precio_oferta = self.precio * factor_descuento
        else:
            precio_oferta = self.precio

        return precio_oferta.quantize(Decimal('0.01'))  # Redondear el precio de oferta a dos decimales


class Comentario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.producto.nombre}"


class Camiseta(Producto):
    codigo_camiseta = models.CharField(max_length=50, unique=True, default="N/A")
    talla = models.CharField(max_length=10)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.color} - Talla: {self.talla}"


class Pantalon(Producto):
    codigo_pantalon = models.CharField(max_length=50, unique=True, default="N/A")
    talla = models.CharField(max_length=10)
    estilo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.estilo} - Talla: {self.talla}"


class Calzado(Producto):
    codigo_calzado = models.CharField(max_length=50, unique=True, default="N/A")
    talla = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.tipo} - Talla: {self.talla}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True, default="N/A")
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

