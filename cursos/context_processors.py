from django.db.models import Sum
from .models import UsuarioLeccion

def puntos_totales_processor(request):
    if request.user.is_authenticated:
        puntos_totales = UsuarioLeccion.objects.filter(usuario=request.user, completada=True).aggregate(total_puntos=Sum('puntos_obtenidos'))['total_puntos'] or 0
    else:
        puntos_totales = 0
    
    return {
        'puntos_totales': puntos_totales,
    }

# Este archivo sirve para meter una variable en todas las vistas, incluso en base. Hay que hacer un cambio en settings.py metiendo
#  'cursos.context_processors.puntos_totales_processor' en 'context_processors': []