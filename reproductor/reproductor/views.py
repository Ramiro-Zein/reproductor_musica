from django.shortcuts import render

# Create your views here.
def inicio(peticion):
    return render(peticion, 'inicio/inicio.html', {})

