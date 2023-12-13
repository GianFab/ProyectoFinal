from django.shortcuts import render
from Clama.models import Camiseta

def lista_camisetas(request):
    camisetas = Camiseta.objects.all()
    return render(request, 'lista_camisetas.html', {'camisetas': camisetas})

def detalle_camiseta(request, camiseta_id):
    camiseta = Camiseta.objects.get(id=camiseta_id)
    return render(request, 'detalle_camiseta.html', {'camiseta': camiseta})