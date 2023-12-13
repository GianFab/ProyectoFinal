from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Camiseta(Producto):
    talla = models.CharField(max_length=10)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.color} - Talla: {self.talla}"


class Pantalon(Producto):
    talla = models.CharField(max_length=10)
    estilo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.estilo} - Talla: {self.talla}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

# Create your models here.
