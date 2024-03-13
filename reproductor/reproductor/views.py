from django.shortcuts import render
# from django.forms.models import model_to_dict
from inicio.models import *

# Create your views here.
# Contiene la lógica para la página de inicio
# Aqui se edita
def inicio(peticion):
    canciones = Cancion.objects.all()
    playlist = Playlist.objects.all()
    return render(peticion, 'inicio/inicio.html', {"canciones": canciones, "playlist": playlist})

def cancion(peticion, id_cancion):
    cancion = Cancion.objects.get(id_cancion=id_cancion)
    cancion.letra = cancion.letra.split(".")
    return render(peticion, "inicio/cancion.html", {"canciones":cancion})