# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Leccion, Curso
from PIL import Image
import os

@receiver(post_save, sender=Curso)
@receiver(post_save, sender=Leccion)
def redimensionar_y_recortar_imagen(sender, instance, **kwargs):
    print("Señal recibida para el modelo Curso")
    try:
        if instance.miniatura:
            print(f"Procesando imagen: {instance.miniatura.path}")
            imagen_path = instance.miniatura.path
            imagen = Image.open(imagen_path)
            
            # Obtener dimensiones originales
            ancho, alto = imagen.size
            print(f"Dimensiones originales: {ancho}x{alto}")

            # Determinar el tamaño mínimo para recortar la imagen al centro
            min_dimension = min(ancho, alto)

            # Calcular coordenadas para recortar la imagen al centro
            izquierda = (ancho - min_dimension) / 2
            superior = (alto - min_dimension) / 2
            derecha = (ancho + min_dimension) / 2
            inferior = (alto + min_dimension) / 2

            # Recortar la imagen
            imagen = imagen.crop((izquierda, superior, derecha, inferior))
            print(f"Imagen recortada a: {min_dimension}x{min_dimension}")

            # Redimensionar la imagen a 512x512 px
            imagen = imagen.resize((512, 512), Image.LANCZOS)
            print("Imagen redimensionada a 512x512")

            # Guardar la imagen
            imagen.save(imagen_path)
            print("Imagen guardada")


    except Exception as e:
        print(f"Error procesando la imagen: {e}")