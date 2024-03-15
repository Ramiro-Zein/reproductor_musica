from django.shortcuts import render
from inicio.models import *

def inicio(peticion):
    canciones = Cancion.objects.all()
    playlist = Playlist.objects.all()
    return render(peticion, 'inicio/inicio.html', {"canciones": canciones, "playlist": playlist})

def cancion(peticion, id_cancion):
    cancion = Cancion.objects.get(id_cancion=id_cancion)
    cancion.letra = cancion.letra.split(".")
    return render(peticion, "inicio/cancion.html", {"cancion":cancion})

def playlist(peticion):
    playlists = Playlist.objects.all()
    return render(peticion, 'inicio/playlist.html', {"playlists": playlists})
