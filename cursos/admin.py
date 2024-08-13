from django.contrib import admin
from .models import Leccion, Curso, Autor, Ejercicio, ImagenLeccion, Pregunta


class ImagenLeccionInline(admin.TabularInline):
    model = ImagenLeccion
    extra = 0  # Define cuántos campos en blanco se mostrarán para agregar nuevas imágenes

class LeccionAdmin(admin.ModelAdmin):
    inlines = [ImagenLeccionInline]

admin.site.register(Leccion, LeccionAdmin)

class LeccionInline(admin.StackedInline):
    model = Leccion
    extra = 0  # Define cuántos campos en blanco se mostrarán para agregar nuevas lecciones

class CursoAdmin(admin.ModelAdmin):
    inlines = [LeccionInline]

admin.site.register(Curso, CursoAdmin)



admin.site.register(Autor)
admin.site.register(Ejercicio)
admin.site.register(Pregunta)
