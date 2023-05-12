from django.shortcuts import render
from django.http import HttpResponse
from core.models import Carrera


def home(request):
    #return HttpResponse("<h1>Home<h1/>")
    return render(request,'core/home.html')


def carrera(request):
    #return HttpResponse("<h1>Carrera<h1/>")
    carreras = Carrera.objects.all()  #Selecciona todo lo de la tabla carrera
    data = {
        'carreras': carreras
    }
    return render(request,'core/carreras.html', data)


def profe(request):
    #return HttpResponse("<h1>Profesores<h1/>" + "<p> SANTUTU MI PROFE <p/>" )
    return render(request,'core/profesores.html')


