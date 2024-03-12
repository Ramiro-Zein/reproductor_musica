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

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, default=True)
    correo = models.CharField(max_length=255, default=True)
    password = models.CharField(max_length=255, default=True)

class Playlist(models.Model):
    id_playlist = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, default=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.TextField(default="")
    imagen = models.CharField(max_length=255, default=True)

class CancionesPlaylist(models.Model):
    id_CancionesPlaylist = models.AutoField(primary_key=True)
    id_cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    id_playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)