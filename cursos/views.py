from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Curso, Leccion, UsuarioLeccion, Cuestionario, Categoria
from django.contrib.auth.decorators import login_required
from django.db.models import Sum  
from .forms import CuestionarioForm

# Create your views here.


def obtener_cursos_realizados(usuario):
    # Obtener los cursos de las lecciones completadas por el usuario
    cursos_realizados_ids = UsuarioLeccion.objects.filter(
        usuario=usuario,
        completada=True
    ).values_list('leccion__curso_id', flat=True).distinct()

    # Verificar que todas las lecciones de esos cursos han sido completadas
    cursos_realizados = []
    for curso_id in cursos_realizados_ids:
        lecciones_del_curso = Leccion.objects.filter(curso_id=curso_id).count()
        lecciones_completadas = UsuarioLeccion.objects.filter(
            usuario=usuario,
            leccion__curso_id=curso_id,
            completada=True
        ).count()

        if lecciones_del_curso == lecciones_completadas:
            cursos_realizados.append(Curso.objects.get(id=curso_id))

    # Devolver los títulos de los cursos realizados
    titulos_cursos = [curso.titulo for curso in cursos_realizados]
    return titulos_cursos

'''
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
    
    
    # Calcular el total de lecciones de todos los cursos
    total_lecciones = sum(conteo for _, conteo, _, _, _ in lecciones_por_curso)

    cursos_realizados = set(obtener_cursos_realizados(request.user))

    # Filtrar los cursos con importancia 3 que no han sido realizados por el usuario
    cursos_importantes_pendientes = Curso.objects.filter(importancia=3).exclude(titulo__in=cursos_realizados).order_by('fecha_creacion')


    return render(request, 'cursos/lista_cursos.html', {'lecciones_por_curso': lecciones_por_curso, 'total_lecciones': total_lecciones, 'cursos_importantes_pendientes': cursos_importantes_pendientes})

'''

@login_required
def lista_cursos(request):
    cursos = Curso.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
    lecciones_por_categoria = {}
    
    for curso in cursos:
        total_lecciones = curso.leccion_set.count()
        lecciones_completadas = UsuarioLeccion.objects.filter(usuario=request.user, leccion__curso=curso, completada=True).count()

        lecciones_completadas_para_puntos = UsuarioLeccion.objects.filter(usuario=request.user, leccion__curso=curso, completada=True)
        total_puntos_completados = lecciones_completadas_para_puntos.aggregate(total_puntos_completados=Sum('puntos_obtenidos'))['total_puntos_completados'] or 0

        lecciones_para_puntos = curso.leccion_set.all()
        total_puntos_curso = lecciones_para_puntos.aggregate(total_puntos_curso=Sum('puntos'))['total_puntos_curso'] or 0

        categoria = curso.categoria
        leccion_info = (curso, total_lecciones, lecciones_completadas, total_puntos_curso, total_puntos_completados)

        if categoria not in lecciones_por_categoria:
            lecciones_por_categoria[categoria] = []

        lecciones_por_categoria[categoria].append(leccion_info)
        
        # Ordenar los cursos en cada categoría: los completados al final
        lecciones_por_categoria[categoria].sort(key=lambda x: x[1] == x[2])

    cursos_realizados = set(obtener_cursos_realizados(request.user))
    cursos_importantes_pendientes = Curso.objects.filter(importancia=3).exclude(titulo__in=cursos_realizados).order_by('fecha_creacion')

    return render(request, 'cursos/lista_cursos.html', {'lecciones_por_categoria': lecciones_por_categoria, 'cursos_importantes_pendientes': cursos_importantes_pendientes})


    

def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    lecciones = Leccion.objects.filter(curso_id=pk)
    cuestinarios = Cuestionario.objects.filter(curso_id=pk)

    lecciones_completadas = {}
    for leccion in lecciones:
        leccion_completada = UsuarioLeccion.objects.filter(usuario=request.user, leccion=leccion, completada=True).exists()
        lecciones_completadas[leccion.id] = leccion_completada
    return render(request, 'cursos/detalle_curso.html', {'curso': curso, 'lecciones':lecciones, 'lecciones_completadas': lecciones_completadas, 'cuestionarios': cuestinarios})

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

def cuestionario_view(request, cuestionario_id):
    cuestionario = get_object_or_404(Cuestionario, id=cuestionario_id)
    if request.method == 'POST':
        form = CuestionarioForm(request.POST, cuestionario=cuestionario)
        if form.is_valid():
            respuestas_correctas = 0
            total_preguntas = cuestionario.pregunta_set.count()

            for pregunta in cuestionario.pregunta_set.all():
                respuesta_usuario = form.cleaned_data.get(f'pregunta_{pregunta.id}')
                respuestas_correctas += comprobar_respuesta(pregunta, respuesta_usuario)
            
            # Aquí puedes guardar el resultado o mostrarlo al usuario
            return redirect('resultado', correctas=respuestas_correctas, total=total_preguntas)
    else:
        form = CuestionarioForm(cuestionario=cuestionario)
    
    return render(request, 'cursos/cuestionario.html', {'form': form, 'cuestionario': cuestionario})

def comprobar_respuesta(pregunta, respuesta_usuario):
    respuestas_correctas = pregunta.respuestas_lista()
    if isinstance(respuesta_usuario, list):
        # Caso de checkbox (varias respuestas correctas)
        return set(respuesta_usuario) == set(respuestas_correctas)
    else:
        # Caso de radio (una sola respuesta correcta)
        return respuesta_usuario == respuestas_correctas[0]
    

def resultado_view(request, correctas, total):
    return render(request, 'cursos/resultado.html', {
        'correctas': correctas,
        'total': total
    })