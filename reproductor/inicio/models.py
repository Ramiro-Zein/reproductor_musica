from django.db import models

class Artista(models.Model):
    id_artista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, default="")


class Album(models.Model):
    id_album = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, default="")
    fecha_lanzamiento = models.CharField(max_length=255, default="")
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=255, default="")

class Cancion(models.Model):
    id_cancion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255, default="")
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    letra = models.TextField(default="")
    duracion = models.CharField(max_length=10, default="")

class Playlist(models.Model):
    id_playlist = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, default=True)
    usuario = models.CharField(max_length=255, default=True)
    descripcion = models.TextField(default="")
    imagen = models.CharField(max_length=255, default=True)