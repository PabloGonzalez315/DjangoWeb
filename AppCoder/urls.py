from django.urls import path
from django.views import *

from AppCoder.views import entregables, home, inicio, profesores,estudiantes,cursos

urlpatterns = [
        path('', inicio),
        path('cursos/', cursos),
        path('entregables/', entregables),
        path('estudiantes/', estudiantes),
        path('profesores/', profesores),
        path('home/', home ),
    
]