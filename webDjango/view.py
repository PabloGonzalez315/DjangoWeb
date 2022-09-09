from django.http import HttpResponse
from django.template import loader

from AppCoder.views import cursos

def home(self,name):
    return HttpResponse(f'hola soy la pagina Home {name}')

def home3(self):
    planilla = loader.get_template('home.html')
    documento = planilla.render()
    return HttpResponse(documento)

def homePage(self):
    lista = [1,2,3,4,5]
    data = {'nombre':'pablo', 'apellido': 'gonzalez', 'lista':lista } 
    planilla = loader.get_template('homepage.html')
    documento = planilla.render(data)
    return HttpResponse(documento)


