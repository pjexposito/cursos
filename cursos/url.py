from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),
    path('curso/<int:pk>/', views.detalle_curso, name='detalle_curso'),
    path('leccion/<int:pk>/', views.detalle_leccion, name='detalle_leccion'),
]