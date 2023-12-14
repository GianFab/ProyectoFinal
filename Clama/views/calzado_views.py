from django.shortcuts import render, redirect
from Clama.models import Calzado
# from Clama.forms import CalzadoForm

def probando(request):
    contexto = {}
    return render(request, 'index.html', contexto)


# Vista para listar todos los calzados
def lista_calzados(request):
    calzados = Calzado.objects.all()
    return render(request, 'lista_calzados.html', {'calzados': calzados})

# Vista para mostrar detalles de un calzado específico
def detalle_calzado(request):
    # calzado = Calzado.objects.get(id=calzado_id)
    return render(request, 'detalle_calzado.html', {'calzado': None})

# Vista para crear un nuevo calzado
# def crear_calzado(request):
#     if request.method == 'POST':
#         form = CalzadoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_calzados')  # Redirige a la lista de calzados
#     else:
#         form = CalzadoForm()
#     return render(request, 'crear_calzado.html', {'form': form})
#
# # Vista para editar un calzado existente
# def editar_calzado(request, calzado_id):
#     calzado = Calzado.objects.get(id=calzado_id)
#     if request.method == 'POST':
#         form = CalzadoForm(request.POST, request.FILES, instance=calzado)
#         if form.is_valid():
#             form.save()
#             return redirect('detalle_calzado', calzado_id=calzado.id)
#     else:
#         form = CalzadoForm(instance=calzado)
#     return render(request, 'editar_calzado.html', {'form': form, 'calzado': calzado})
#
# # Vista para eliminar un calzado existente
# def eliminar_calzado(request, calzado_id):
#     calzado = Calzado.objects.get(id=calzado_id)
#     if request.method == 'POST':
#         calzado.delete()
#         return redirect('lista_calzados')  # Redirige a la lista de calzados
#     return render(request, 'confirmar_eliminar_calzado.html', {'calzado': calzado})
