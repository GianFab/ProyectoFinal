from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView, ListView

from Clama.forms.pantalon_form import *
from Clama.models import Pantalon

class ListaPantalones(LoginRequiredMixin, ListView):
    model = Pantalon
    template_name = 'lista_pantalones.html'
    context_object_name = 'pantalones_con_oferta'
    form_class = BusquedaPantalonForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pantalones = self.get_queryset()
        precios_oferta = [pantalon.precio_oferta() for pantalon in pantalones]
        context['pantalones_con_oferta'] = zip(pantalones, precios_oferta)
        context['form'] = self.form_class()
        return context


# Vista para mostrar detalles de un pantalon específico
class DetallePantalon(LoginRequiredMixin, DetailView):
    model = Pantalon
    template_name = 'detalle_pantalon.html'
    context_object_name = 'pantalon'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['precio_oferta'] = self.object.precio_oferta()
        context['comentarios'] = self.object.comentarios.all()
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Pantalon, pk=self.kwargs.get('pantalon_id'))


class BusquedaPantalon(LoginRequiredMixin, View):
    def get(self, request):
        codigo_pantalon = request.GET.get('codigo_pantalon')
        pantalon = get_object_or_404(Pantalon, codigo_pantalon=codigo_pantalon)
        return HttpResponseRedirect(reverse('detalle_pantalon', kwargs={'pantalon_id': pantalon.id}))


# Vista para crear un nuevo pantalon
class CrearPantalon(LoginRequiredMixin, View):
    template_name = 'crear_pantalon.html'

    def get(self, request):
        form = PantalonForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PantalonForm(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            pantalon = Pantalon(
                nombre=informacion['nombre'],
                precio=informacion['precio'],
                descripcion=informacion['descripcion'],
                oferta=informacion['oferta'],
                imagen=informacion['imagen'],
                codigo_pantalon=informacion['codigo_pantalon'],
                talla=informacion['talla'],
                estilo=informacion['estilo']
            )
            pantalon.save()
            return redirect('/app/pantalon/' + str(pantalon.id))
        return render(request, self.template_name, {'form': form})


class EditarPantalon(LoginRequiredMixin, View):
    template_name = 'editar_pantalon.html'

    def get(self, request, pantalon_id):
        pantalon = Pantalon.objects.get(id=pantalon_id)
        form = PantalonForm(initial={
            'nombre': pantalon.nombre,
            'precio': pantalon.precio,
            'descripcion': pantalon.descripcion,
            'oferta': pantalon.oferta,
            'imagen': pantalon.imagen,
            'codigo_pantalon': pantalon.codigo_pantalon,
            'talla': pantalon.talla,
            'estilo': pantalon.estilo
        })
        return render(request, self.template_name, {'form': form, 'pantalon': pantalon})

    def post(self, request, pantalon_id):
        pantalon = Pantalon.objects.get(id=pantalon_id)
        form = PantalonForm(request.POST, request.FILES)

        if form.is_valid():
            pantalon.nombre = form.cleaned_data['nombre']
            pantalon.precio = form.cleaned_data['precio']
            pantalon.descripcion = form.cleaned_data['descripcion']
            pantalon.oferta = form.cleaned_data['oferta']
            pantalon.imagen = form.cleaned_data['imagen']
            pantalon.codigo_pantalon = form.cleaned_data['codigo_pantalon']
            pantalon.talla = form.cleaned_data['talla']
            pantalon.estilo = form.cleaned_data['estilo']
            pantalon.save()
            return redirect('/app/pantalon/' + str(pantalon.id))

        return render(request, self.template_name, {'form': form, 'pantalon': pantalon})
#


# # Vista para eliminar un pantalon existente
class EliminarPantalon(LoginRequiredMixin, View):
    template_name = 'eliminar_pantalon.html'
    success_url = reverse_lazy('pantalones')  # Redirige a la lista de pantalones

    def get(self, request, pantalon_id):
        pantalon = Pantalon.objects.get(id=pantalon_id)
        return render(request, self.template_name, {'pantalon': pantalon})

    def post(self, request, pantalon_id):
        pantalon = Pantalon.objects.get(id=pantalon_id)
        pantalon.delete()
        return redirect(self.success_url)