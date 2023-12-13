from django.shortcuts import render
from Clama.models import Producto, Camiseta, Pantalon, Usuario

# PRODUCTO
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

# CAMISETA
def lista_camisetas(request):
    camisetas = Camiseta.objects.all()
    return render(request, 'lista_camisetas.html', {'camisetas': camisetas})

def detalle_camiseta(request, camiseta_id):
    camiseta = Camiseta.objects.get(id=camiseta_id)
    return render(request, 'detalle_camiseta.html', {'camiseta': camiseta})

# PANTALONES
def lista_pantalones(request):
    pantalones = Pantalon.objects.all()
    return render(request, 'lista_pantalones.html', {'pantalones': pantalones})

def detalle_pantalon(request, pantalon_id):
    pantalon = Pantalon.objects.get(id=pantalon_id)
    return render(request, 'detalle_pantalon.html', {'pantalon': pantalon})

# USUARIOS
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

def detalle_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    return render(request, 'detalle_usuario.html', {'usuario': usuario})
