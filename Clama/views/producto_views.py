from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from Clama.forms.producto_form import BusquedaProductoForm
from Clama.models import Producto


class ListaProductos(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'lista_productos.html'
    context_object_name = 'productos_con_oferta'
    form_class = BusquedaProductoForm

    def get_queryset(self):
        return Producto.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productos = self.get_queryset()
        precios_oferta = [producto.precio_oferta() for producto in productos]
        context['productos_con_oferta'] = zip(productos, precios_oferta)
        context['form'] = self.form_class()
        return context
