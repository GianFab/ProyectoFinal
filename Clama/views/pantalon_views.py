from django.shortcuts import render
from Clama.models import Pantalon

def lista_pantalones(request):
    pantalones = Pantalon.objects.all()
    return render(request, 'lista_pantalones.html', {'pantalones': pantalones})

def detalle_pantalon(request, pantalon_id):
    pantalon = Pantalon.objects.get(id=pantalon_id)
    return render(request, 'detalle_pantalon.html', {'pantalon': pantalon})