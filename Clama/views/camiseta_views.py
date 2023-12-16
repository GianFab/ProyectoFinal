from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView

from Clama.forms.camiseta_form import CamisetaForm, BusquedaCamisetaForm
from Clama.models import Camiseta

class ListaCamisetas(LoginRequiredMixin, ListView):
    model = Camiseta
    template_name = 'lista_camisetas.html'
    context_object_name = 'camisetas_con_oferta'
    form_class = BusquedaCamisetaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        camisetas = self.get_queryset()
        precios_oferta = [camiseta.precio_oferta() for camiseta in camisetas]
        context['camisetas_con_oferta'] = zip(camisetas, precios_oferta)
        context['form'] = self.form_class()
        return context


class DetalleCamiseta(LoginRequiredMixin, DetailView):
    model = Camiseta
    template_name = 'detalle_camiseta.html'
    context_object_name = 'camiseta'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['precio_oferta'] = self.object.precio_oferta()
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Camiseta, pk=self.kwargs.get('camiseta_id'))


class BusquedaCamiseta(LoginRequiredMixin, View):
    def get(self, request):
        codigo_camiseta = request.GET.get('codigo_camiseta')
        camiseta = get_object_or_404(Camiseta, codigo_camiseta=codigo_camiseta)
        return HttpResponseRedirect(reverse('detalle_camiseta', kwargs={'camiseta_id': camiseta.id}))



class CrearCamiseta(LoginRequiredMixin, View):
    template_name = 'crear_camiseta.html'

    def get(self, request):
        form = CamisetaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CamisetaForm(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            camiseta = Camiseta(
                nombre=informacion['nombre'],
                precio=informacion['precio'],
                descripcion=informacion['descripcion'],
                oferta=informacion['oferta'],
                imagen=informacion['imagen'],
                codigo_camiseta=informacion['codigo_camiseta'],
                talla=informacion['talla'],
                color=informacion['color']
            )
            camiseta.save()
            return redirect('/app/camiseta/' + str(camiseta.id))
        return render(request, self.template_name, {'form': form})



class EditarCamiseta(LoginRequiredMixin, View):
    template_name = 'editar_camiseta.html'

    def get(self, request, camiseta_id):
        camiseta = Camiseta.objects.get(id=camiseta_id)
        form = CamisetaForm(initial={
            'nombre': camiseta.nombre,
            'precio': camiseta.precio,
            'descripcion': camiseta.descripcion,
            'oferta': camiseta.oferta,
            'imagen': camiseta.imagen,
            'codigo_camiseta': camiseta.codigo_camiseta,
            'talla': camiseta.talla,
            'color': camiseta.color
        })
        return render(request, self.template_name, {'form': form, 'camiseta': camiseta})

    def post(self, request, camiseta_id):
        camiseta = Camiseta.objects.get(id=camiseta_id)
        form = CamisetaForm(request.POST, request.FILES)

        if form.is_valid():
            camiseta.nombre = form.cleaned_data['nombre']
            camiseta.precio = form.cleaned_data['precio']
            camiseta.descripcion = form.cleaned_data['descripcion']
            camiseta.oferta = form.cleaned_data['oferta']
            camiseta.imagen = form.cleaned_data['imagen']
            camiseta.codigo_camiseta = form.cleaned_data['codigo_camiseta']
            camiseta.talla = form.cleaned_data['talla']
            camiseta.color = form.cleaned_data['color']
            camiseta.save()
            return redirect('/app/camiseta/' + str(camiseta.id))

        return render(request, self.template_name, {'form': form, 'camiseta': camiseta})
#



class EliminarCamiseta(LoginRequiredMixin, View):
    template_name = 'eliminar_camiseta.html'
    success_url = reverse_lazy('camisetas')

    def get(self, request, camiseta_id):
        camiseta = Camiseta.objects.get(id=camiseta_id)
        return render(request, self.template_name, {'camiseta': camiseta})

    def post(self, request, camiseta_id):
        camiseta = Camiseta.objects.get(id=camiseta_id)
        camiseta.delete()
        return redirect(self.success_url)