from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe

class Leccion(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    contenido = models.TextField()
    puntos = models.SmallIntegerField()
    ejercicio = models.ForeignKey('Ejercicio', on_delete=models.CASCADE, blank=True, null=True)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    miniatura = models.ImageField(upload_to='images/miniaturas/')
    imagen1 = models.ImageField(upload_to='images/lecciones/')
    imagen2 = models.ImageField(upload_to='images/lecciones/')
    imagen3 = models.ImageField(upload_to='images/lecciones/')
    imagen4 = models.ImageField(upload_to='images/lecciones/')
    imagen5 = models.ImageField(upload_to='images/lecciones/')

    @property
    def contenido_con_imagenes(self):
        contenido_actualizado = self.contenido
        for i in range(1, 6):
            imagen = getattr(self, f'imagen{i}')
            if imagen:
                valor = f'<img src="{imagen.url}" alt="imagen{i}" />'
            else:
                valor = ''
            contenido_actualizado = contenido_actualizado.replace(f'** imagen{i} **', valor)
        return mark_safe(contenido_actualizado)

    def publicar(self):
        self.fecha_creacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    
class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    explicacion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    puntos = models.SmallIntegerField()
    miniatura = models.ImageField(upload_to='images/miniaturas/')


    def publicar(self):
        self.fecha_creacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    

class Ejercicio(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(default=timezone.now)
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