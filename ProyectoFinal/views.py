from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):
    return HttpResponse("Probando")


def saludo_nombre(request, nombre):
    return HttpResponse(f"{nombre} AKiiiiiiiiii")


def saludo_plantilla(request):
    contexto = {
        "nombre": "Jorge",
        "apellido": "Salvaje",
    }
    return render(request, "index.html", contexto)

