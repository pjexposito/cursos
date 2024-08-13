from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),
    path('curso/<int:pk>/', views.detalle_curso, name='detalle_curso'),
    path('leccion/<int:pk>/', views.detalle_leccion, name='detalle_leccion'),
    path('leccion/<int:leccion_id>/completar/', views.marcar_leccion_completada, name='marcar_leccion_completada'),
    path('cuestionario/', views.cuestionario_view, name='cuestionario'),
]