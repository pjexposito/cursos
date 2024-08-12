from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from .utils import transformar_texto_oculto
import markdown2

class Leccion(models.Model):
    titulo = models.CharField(max_length=100)
    explicacion = models.CharField(max_length=400)

    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    fecha_creacion = models.DateField(default=timezone.now)
    contenido = models.TextField()
    puntos = models.SmallIntegerField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    miniatura = models.ImageField(upload_to='images/miniaturas/')


    @property
    def contenido_con_imagenes(self):
        contenido_actualizado = self.contenido
        for i, imagen in enumerate(self.imagenes.all(), start=1):
            valor = f'<img src="{imagen.imagen.url}" alt="imagen{i}" />'
            contenido_actualizado = contenido_actualizado.replace(f'** imagen{i} **', valor)
        contenido_actualizado = transformar_texto_oculto(contenido_actualizado)
        contenido_actualizado = markdown2.markdown(contenido_actualizado)

        return mark_safe(contenido_actualizado)  # Importante marcarlo como seguro si se va a renderizar en HTML

    def publicar(self):
        self.fecha_creacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    
class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    explicacion = models.CharField(max_length=400)
    miniexplicacion = models.TextField()
    duracion = models.PositiveIntegerField()  # Duración en minutos
    fecha_creacion = models.DateField(default=timezone.now)
    puntos = models.SmallIntegerField()
    miniatura = models.ImageField(upload_to='images/miniaturas/')


    def publicar(self):
        self.fecha_creacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    

class Ejercicio(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_creacion = models.DateField(default=timezone.now)
    puntos = models.SmallIntegerField()
    oportunidades = models.SmallIntegerField()
    logica = models.TextField()

    def publicar(self):
        self.fecha_creacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    nvend = models.CharField(max_length=200)

    def publicar(self):
        self.save()

    def __str__(self):
        return self.nombre
    
class UsuarioLeccion(models.Model):
    usuario = models.ForeignKey(User, related_name='lecciones_completadas', on_delete=models.CASCADE)
    leccion = models.ForeignKey(Leccion, related_name='usuarios_completaron', on_delete=models.CASCADE)
    completada = models.BooleanField(default=False)
    fecha_completada = models.DateField(null=True, blank=True)
    puntos_obtenidos = models.SmallIntegerField()
    def __str__(self):
        return f'{self.usuario.username} - {self.leccion.titulo}'
    
class ImagenLeccion(models.Model):
    leccion = models.ForeignKey(Leccion, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='images/lecciones/')