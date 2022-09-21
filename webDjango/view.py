from django.http import HttpResponse
from django.template import loader

from AppCoder.views import cursos


def homepage(self):
    planilla = loader.get_template('homepage.html')
    documento = planilla.render()
    return HttpResponse(documento)



