from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView

from Clama.models import Calzado
from Clama.forms.calzado_form import *

class ListaCalzados(LoginRequiredMixin, ListView):
    model = Calzado
    template_name = 'lista_calzados.html'
    context_object_name = 'calzados_con_oferta'
    form_class = BusquedaCalzadoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calzados = self.get_queryset()
        precios_oferta = [calzado.precio_oferta() for calzado in calzados]
        context['calzados_con_oferta'] = zip(calzados, precios_oferta)
        context['form'] = self.form_class()
        return context


# Vista para mostrar detalles de un calzado específico
class DetalleCalzado(LoginRequiredMixin, DetailView):
    model = Calzado
    template_name = 'detalle_calzado.html'
    context_object_name = 'calzado'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['precio_oferta'] = self.object.precio_oferta()
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Calzado, pk=self.kwargs.get('calzado_id'))


class BusquedaCalzado(LoginRequiredMixin, View):
    def get(self, request):
        codigo_calzado = request.GET.get('codigo_calzado')
        calzado = get_object_or_404(Calzado, codigo_calzado=codigo_calzado)
        return HttpResponseRedirect(reverse('detalle_calzado', kwargs={'calzado_id': calzado.id}))


# Vista para crear un nuevo calzado
class CrearCalzado(LoginRequiredMixin, View):
    template_name = 'crear_calzado.html'

    def get(self, request):
        form = CalzadoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
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
            calzado.usuario = request.user
            calzado.save()
            return redirect('/app/calzado/' + str(calzado.id))
        return render(request, self.template_name, {'form': form})


class EditarCalzado(LoginRequiredMixin, View):
    template_name = 'editar_calzado.html'

    def get(self, request, calzado_id):
        calzado = Calzado.objects.get(id=calzado_id)
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
        return render(request, self.template_name, {'form': form, 'calzado': calzado})

    def post(self, request, calzado_id):
        calzado = Calzado.objects.get(id=calzado_id)
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
            calzado.usuario = request.user
            calzado.save()
            return redirect('/app/calzado/' + str(calzado.id))

        return render(request, self.template_name, {'form': form, 'calzado': calzado})
#



class EliminarCalzado(LoginRequiredMixin, View):
    template_name = 'eliminar_calzado.html'
    success_url = reverse_lazy('calzados')  # Redirige a la lista de calzados

    def get(self, request, calzado_id):
        calzado = Calzado.objects.get(id=calzado_id)
        return render(request, self.template_name, {'calzado': calzado})

    def post(self, request, calzado_id):
        calzado = Calzado.objects.get(id=calzado_id)
        calzado.delete()
        return redirect(self.success_url)