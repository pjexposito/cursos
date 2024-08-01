from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Curso, Leccion

# Create your views here.
def lista_cursos(request):
    cursos = Curso.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
    # Inicializa un diccionario para almacenar el conteo de lecciones por curso
    # Crear una lista de tuplas (curso, conteo de lecciones)
    lecciones_por_curso = [(curso, curso.leccion_set.count()) for curso in cursos]
    
    # Calcular el total de lecciones
    total_lecciones = sum(conteo for _, conteo in lecciones_por_curso)

    return render(request, 'cursos/lista_cursos.html', {'lecciones_por_curso': lecciones_por_curso, 'total_lecciones': total_lecciones})

def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    lecciones = Leccion.objects.filter(curso_id=pk)
    return render(request, 'cursos/detalle_curso.html', {'curso': curso, 'lecciones':lecciones})

def detalle_leccion(request, pk):
    leccion = get_object_or_404(Leccion, pk=pk)
    curso = get_object_or_404(Curso, id=leccion.curso_id)
    return render(request, 'cursos/detalle_leccion.html', {'leccion': leccion, 'curso': curso})