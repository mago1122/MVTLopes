from django.http import HttpResponse
from django.template import Template
from datetime import datetime
from django.shortcuts import render
from appfamiliar.models import *


# Create your views here.

def listado_familia(request):
    familiar = Familiar.objects.all()

    cadena_respuesta = ""

    for a in familiar:
        cadena_respuesta += a.nombre + " " + a.apellido + " " + "DNI: " + str(a.dni) + " - Fecha de nacimiento: " + str(a.fecha_nac) + " | "

    return HttpResponse(cadena_respuesta)


