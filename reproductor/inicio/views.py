from django.shortcuts import render
# from django.forms.models import model_to_dict
from inicio.models import *


# Create your views here.
# Contiene la lógica para la página de inicio
def inicio(peticion):
    canciones = Cancion.objects.all()

    playlist = Playlist.objects.all()

    return render(peticion, 'inicio/inicio.html', {"canciones": canciones, "playlist": playlist})

