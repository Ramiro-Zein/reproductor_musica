from django.shortcuts import render
# from django.forms.models import model_to_dict
from inicio.models import *

# Create your views here.
# Contiene la lógica para la página de inicio

def inicio(peticion):
    return render(peticion, 'inicio/inicio.html', {})

