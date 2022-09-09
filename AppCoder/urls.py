from django.urls import path
from django.views import *

from AppCoder.views import entregables, inicio, profesores,estudiantes,cursos

urlpatterns = [
        path('', inicio),
        path('cursos/', cursos),
        path('entregables/', entregables),
        path('estudaiantes/', estudiantes),
        path('profesores/', profesores),
    
]