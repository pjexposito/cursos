from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Curso, Leccion, UsuarioLeccion
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
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
    lecciones_completadas = {}
    for leccion in lecciones:
        leccion_completada = UsuarioLeccion.objects.filter(usuario=request.user, leccion=leccion, completada=True).exists()
        lecciones_completadas[leccion.id] = leccion_completada
    return render(request, 'cursos/detalle_curso.html', {'curso': curso, 'lecciones':lecciones, 'lecciones_completadas': lecciones_completadas})

def detalle_leccion(request, pk):
    leccion = get_object_or_404(Leccion, pk=pk)
    curso = get_object_or_404(Curso, id=leccion.curso_id)

    return render(request, 'cursos/detalle_leccion.html', {'leccion': leccion, 'curso': curso})

@login_required
def marcar_leccion_completada(request, leccion_id):
    leccion = get_object_or_404(Leccion, id=leccion_id)
    UsuarioLeccion.objects.update_or_create(
        usuario=request.user, leccion=leccion,
        defaults={'completada': True, 'fecha_completada': timezone.now()}
    )
    return redirect('lista_cursos')