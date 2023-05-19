from django.shortcuts import render
from django.http import HttpResponse
from core.models import Carrera,Docente



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
    docentes = Docente.objects.all()
    data = {
        'docentes': docentes
    }
    return render(request,'core/profesores.html',data)

def nueva_carrera(request):

    if request.POST:
        nombre = request.POST['nombre']
        identi = request.POST['identificador']
        duracion= request.POST['semestres']

        c = Carrera(codigo=identi,nombre_carrera=nombre,duracion_semestres=duracion)
        c.save()

    return render(request,'core/nueva_carrera.html')

def nueva_profesores(request):
    if request.POST:
        nombre= request.POST['nombre']
        apellido= request.POST['apellido']
        email= request.POST['email']
        p = Docente(nombre=nombre ,apellido= apellido ,email= email)
        p.save()

    return render(request,'core/nueva_profesores.html')
