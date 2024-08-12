from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Curso, Leccion, UsuarioLeccion
from django.contrib.auth.decorators import login_required
from django.db.models import Sum  

# Create your views here.

@login_required
def lista_cursos(request):
    cursos = Curso.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
    lecciones_por_curso = []
    
    for curso in cursos:
        # Contar el número de lecciones totales del curso
        total_lecciones = curso.leccion_set.count()
        
        # Contar el número de lecciones completadas por el usuario
        lecciones_completadas = UsuarioLeccion.objects.filter(usuario=request.user, leccion__curso=curso, completada=True).count()

        lecciones_completadas_para_puntos = UsuarioLeccion.objects.filter(usuario=request.user, leccion__curso=curso, completada=True)
        total_puntos_completados = lecciones_completadas_para_puntos.aggregate(total_puntos_completados=Sum('puntos_obtenidos'))['total_puntos_completados'] or 0


        # Cuenta el total de puntos que tiene el curso
        lecciones_para_puntos = curso.leccion_set.all()  # Obtener todas las lecciones asociadas al curso
        total_puntos_curso = lecciones_para_puntos.aggregate(total_puntos_curso=Sum('puntos'))['total_puntos_curso'] or 0

        # Agregar una tupla al resultado con el curso, número de lecciones totales y lecciones completadas
        lecciones_por_curso.append((curso, total_lecciones, lecciones_completadas,total_puntos_curso, total_puntos_completados))
        lecciones_por_curso.sort(key=lambda x: x[1] == x[2])  # Pone los completados al final
        #Esta parte de arriba está hecha por ChatGPT. No entiendo como lo ha hecho. Investigar.
    # Calcular el total de lecciones de todos los cursos
    total_lecciones = sum(conteo for _, conteo, _, _, _ in lecciones_por_curso)


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
        defaults={'completada': True, 'fecha_completada': timezone.now(), 'puntos_obtenidos': leccion.puntos}
    )
    return redirect('lista_cursos')