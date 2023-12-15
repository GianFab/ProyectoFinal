from django.shortcuts import render, redirect
from Clama.models import Calzado
from django.views.generic import CreateView
from Clama.forms.calzado_form import *

def probando(request):
    contexto = {}
    return render(request, 'index.html', contexto)


# Vista para listar todos los calzados
def lista_calzados(request):
    calzados = Calzado.objects.all()
    precios_oferta = [calzado.precio_oferta() for calzado in calzados]

    calzados_con_oferta = zip(calzados, precios_oferta)

    return render(request, 'lista_calzados.html', {'calzados_con_oferta': calzados_con_oferta, 'form': BusquedaCalzadoForm()})


# Vista para mostrar detalles de un calzado específico
def detalle_calzado(request, calzado_id):
    calzado = Calzado.objects.get(id=calzado_id)
    precio_oferta = calzado.precio_oferta()
    return render(request, 'detalle_calzado.html', {'calzado': calzado, 'precio_oferta': precio_oferta})


def busqueda_calzado(request):
    codigo_calzado = request.GET['codigo_calzado']
    calzado = Calzado.objects.get(codigo_calzado=codigo_calzado)
    return redirect('/app/calzado/' + str(calzado.id))


# Vista para crear un nuevo calzado
def crear_calzado(request):
    if request.method == 'POST':
        form = CalzadoForm(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            calzado = Calzado(
                nombre=informacion['nombre'],
                precio=informacion['precio'],
                descripcion=informacion['descripcion'],
                oferta=informacion['oferta'],
                imagen=informacion['imagen'],
                codigo_calzado=informacion['codigo_calzado'],
                talla=informacion['talla'],
                tipo=informacion['tipo']
            )
            calzado.save()
            return redirect('/app/calzado/' + str(calzado.id))
    else:
        form = CalzadoForm()
    return render(request, 'crear_calzado.html', {'form': form})


# # Vista para editar un calzado existente
def editar_calzado(request, calzado_id):
    calzado = Calzado.objects.get(id=calzado_id)

    if request.method == 'POST':
        form = CalzadoForm(request.POST, request.FILES)

        if form.is_valid():
            calzado.nombre = form.cleaned_data['nombre']
            calzado.precio = form.cleaned_data['precio']
            calzado.descripcion = form.cleaned_data['descripcion']
            calzado.oferta = form.cleaned_data['oferta']
            calzado.imagen = form.cleaned_data['imagen']
            calzado.codigo_calzado = form.cleaned_data['codigo_calzado']
            calzado.talla = form.cleaned_data['talla']
            calzado.tipo = form.cleaned_data['tipo']
            calzado.save()

            return redirect('/app/calzado/' + str(calzado.id))
    else:
        form = CalzadoForm(initial={
            'nombre': calzado.nombre,
            'precio': calzado.precio,
            'descripcion': calzado.descripcion,
            'oferta': calzado.oferta,
            'imagen': calzado.imagen,
            'codigo_calzado': calzado.codigo_calzado,
            'talla': calzado.talla,
            'tipo': calzado.tipo
        })

    return render(request, 'editar_calzado.html', {'form': form, 'calzado': calzado})
#
# # Vista para eliminar un calzado existente
def eliminar_calzado(request, calzado_id):
    calzado = Calzado.objects.get(id=calzado_id)
    if request.method == 'POST':
        calzado.delete()
        return redirect('/app/calzados/')  # Redirige a la lista de calzados
    return render(request, 'eliminar_calzado.html', {'calzado': calzado})
