from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from Clama.forms.comentario_form import ComentarioForm
from Clama.models import Calzado, Comentario, Pantalon, Camiseta


class AgregarComentarioCalzado(LoginRequiredMixin, View):
    def post(self, request, calzado_id):
        calzado = get_object_or_404(Calzado, pk=calzado_id)
        form = ComentarioForm(request.POST)

        if form.is_valid():
            texto = form.cleaned_data['texto']
            # Crear un nuevo comentario asociado a este calzado y usuario actual
            Comentario.objects.create(producto=calzado, usuario=request.user, texto=texto)
            return redirect('detalle_calzado', calzado_id=calzado_id)

        # Si hay errores en el formulario, volver a mostrar el detalle del calzado con los errores
        return render(request, 'detalle_calzado.html', {'calzado': calzado, 'form': form})


class AgregarComentarioPantalon(LoginRequiredMixin, View):
    def post(self, request, pantalon_id):
        pantalon = get_object_or_404(Pantalon, pk=pantalon_id)
        form = ComentarioForm(request.POST)

        if form.is_valid():
            texto = form.cleaned_data['texto']

            Comentario.objects.create(producto=pantalon, usuario=request.user, texto=texto)
            return redirect('detalle_pantalon', pantalon_id=pantalon_id)

        return render(request, 'detalle_pantalon.html', {'pantalon': pantalon, 'form': form})


class AgregarComentarioCamiseta(LoginRequiredMixin, View):
    def post(self, request, camiseta_id):
        camiseta = get_object_or_404(Camiseta, pk=camiseta_id)
        form = ComentarioForm(request.POST)

        if form.is_valid():
            texto = form.cleaned_data['texto']

            Comentario.objects.create(producto=camiseta, usuario=request.user, texto=texto)
            return redirect('detalle_camiseta', camiseta_id=camiseta_id)

        return render(request, 'detalle_camiseta.html', {'camiseta': camiseta, 'form': form})
