from django.db import models

# Create your models here.

class docente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.CharField(max_length=30)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Carrera(models.Model):
    codigo= models.CharField(max_length=10)
    nombre_carrera= models.CharField(max_length=50)
    duracion_semestres= models.IntegerField()
    #jefe_carrera = models.ForeignKey(docente, on_delete=models.CASCADE)



    def __str__(self):
        return self.nombre_carrera


# Charfield= texto, caja de texto