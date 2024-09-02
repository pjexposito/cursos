from django.contrib import admin
from .models import Leccion, Curso, Autor, Ejercicio, ImagenLeccion, Pregunta, Cuestionario, Categoria


class ImagenLeccionInline(admin.TabularInline):
    model = ImagenLeccion
    extra = 0  # Define cuántos campos en blanco se mostrarán para agregar nuevas imágenes

class LeccionAdmin(admin.ModelAdmin):
    inlines = [ImagenLeccionInline]


class LeccionInline(admin.StackedInline):
    model = Leccion
    extra = 0  # Define cuántos campos en blanco se mostrarán para agregar nuevas lecciones

class CursoAdmin(admin.ModelAdmin):
    inlines = [LeccionInline]

class PreguntaInline(admin.StackedInline):
    model = Pregunta
    extra = 0  # Define cuántos campos en blanco se mostrarán para agregar nuevas lecciones

class CuestionarioAdmin(admin.ModelAdmin):
    inlines = [PreguntaInline]

admin.site.register(Curso, CursoAdmin)
admin.site.register(Leccion, LeccionAdmin)
admin.site.register(Cuestionario, CuestionarioAdmin)
admin.site.register(Autor)
admin.site.register(Categoria)
