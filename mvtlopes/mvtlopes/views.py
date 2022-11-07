from django.http import HttpResponse
from appfamiliar.models import *
from django.template import Template, Context
from datetime import datetime

def vista_familiares(request):
    miembro = Familiar.objects.all()
    
    datos = {"consigna": "desafio", "miembros": miembro}

    archivo = open(r"mvtlopes\templates\plantilla.html")

    plantilla = Template(archivo.read())

    archivo.close()

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)
    