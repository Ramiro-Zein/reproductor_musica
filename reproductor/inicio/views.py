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

def playlist(peticion, id_playlist):
    playlist_datos = Playlist.objects.get(id_playlist=id_playlist)
    canciones_playlist = CancionesPlaylist.objects.get(id_playlist=id_playlist)
    return render(peticion, 'inicio/playlist.html', {"playlist_datos": playlist_datos})

