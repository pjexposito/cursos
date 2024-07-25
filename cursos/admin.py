from django.contrib import admin
from .models import Leccion, Curso, Autor, Ejercicio

admin.site.register(Leccion)
admin.site.register(Curso)
admin.site.register(Autor)
admin.site.register(Ejercicio)