from django.contrib import admin
from core.models import Carrera,docente             #Se importan el modelo

# Register your models here.

class CarreraAdmin(admin.ModelAdmin):
    pass

class DocenteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Carrera,CarreraAdmin)   # Permite gestionar la tabla carreras
admin.site.register(docente,DocenteAdmin)