from django.shortcuts import render
from Clama.models import Usuario

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

def detalle_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    return render(request, 'detalle_usuario.html', {'usuario': usuario})