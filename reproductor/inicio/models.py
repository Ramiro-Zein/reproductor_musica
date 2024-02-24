from django.db import models

# Tabla: Artista
class Artista(models.Model):
    # Campo de ID que se autoincrementa.
    id_artista = models.AutoField(primary_key=True)
    # Campo para el nombre del artista.
    nombre = models.CharField(max_length=255)
    # Campo para el género del artista.
    genero = models.CharField(max_length=255, null=True)
    # Campo para la imagen del artista.
    imagen = models.ImageField(upload_to='imagenes/')
    # Campo para el número de seguidores del artista.
    seguidores = models.IntegerField()
    # Discografía del artista. Puede ser NULL.
    discografia = models.CharField(max_length=255, null=True, blank=True)
    # Número de oyentes mensuales del artista. Puede ser NULL.
    oyentes_mensuales = models.IntegerField(null=True, blank=True)
    # Relación muchos a muchos con Album. Un Artista puede tener muchos Albums y un Album puede estar asociado con muchos Artistas.
    albums = models.ManyToManyField('Album', related_name='artistas_albums')


# Tabla: Album
class Album(models.Model):
    # Campo de ID que se autoincrementa.
    id_album = models.AutoField(primary_key=True)
    # Relación muchos a uno con Artista. Si se elimina un Artista, se eliminan los Álbumes asociados.
    artista = models.ForeignKey('Artista', on_delete=models.CASCADE)
    # Campo para el título del álbum.
    titulo = models.CharField(max_length=255)
    # Campo para la imagen del álbum.
    imagen = models.ImageField(upload_to='imagenes/')
    # Año de lanzamiento del álbum.
    ano_lanzamiento = models.DateField()
    # Número de canciones en el álbum.
    numero_canciones = models.IntegerField()


# Tabla: Canción
class Cancion(models.Model):
    # Campo de ID que se autoincrementa.
    id_cancion = models.AutoField(primary_key=True)
    # Campo para el título de la canción.
    titulo = models.CharField(max_length=255)
    # Relación muchos a uno con Artista. Si se elimina un Artista, se eliminan las Canciones asociadas.
    artista = models.ForeignKey('Artista', on_delete=models.CASCADE)
    # Relación muchos a uno con Album. Si se elimina un Album, se eliminan las Canciones asociadas.
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    # Campo para la imagen de la canción.
    imagen = models.ImageField(upload_to='imagenes/')
    # Campo para la fecha de creación de la canción. Se establece automáticamente al crear la canción.
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # Campo para el número de "me gusta" de la canción.
    me_gusta = models.IntegerField()
    # Duración de la canción o playlist.
    duracion = models.DurationField(null=True)
    # Género de la canción o playlist, puede ser NULL.
    genero = models.CharField(max_length=255, null=True, blank=True)


# Tabla: Playlist
class Playlist(models.Model):
    # Campo de ID que se autoincrementa.
    id_playlist = models.AutoField(primary_key=True)
    # Campo para el nombre de la playlist.
    nombre = models.CharField(max_length=255)
    # Campo para la imagen de la playlist.
    imagen = models.ImageField(upload_to='imagenes/')
    # Relación muchos a muchos con Cancion. Una Playlist puede tener muchas Canciones y una Cancion puede estar en muchas Playlists.
    id_cancion = models.ManyToManyField(Cancion)
    # Usuario que creó la playlist.
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    # Artista dentro de la playlist.
    id_artista = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    # Indica si la playlist es pública (True) o privada (False).
    publica_privada = models.BooleanField(default=True)


# Tabla: Usuario
class Usuario(models.Model):
    # Campo de ID que se autoincrementa.
    id_usuario = models.AutoField(primary_key=True)
    # Campo para el nombre de usuario.
    nombre_usuario = models.CharField(max_length=255)
    # Campo para el correo electrónico del usuario.
    correo = models.EmailField()
    # Relación muchos a muchos con Playlist. Un Usuario puede tener muchas Playlists y una Playlist puede estar asociada con muchos Usuarios.
    playlists = models.ManyToManyField(Playlist, related_name='usuarios_playlists')
    # Campo para la imagen del usuario.
    imagen = models.ImageField(upload_to='imagenes/')
    # Campo para el tipo de cuenta del usuario.
    tipo_cuenta = models.CharField(max_length=20)
    # Relación muchos a muchos con Usuario para los usuarios seguidos por el usuario actual. Un Usuario puede seguir a muchos Usuarios y un Usuario puede ser seguido por muchos Usuarios.
    seguidos = models.ManyToManyField('Usuario', related_name='seguidos', blank=True)
    # Relación muchos a muchos con Usuario para los seguidores del usuario actual. Un Usuario puede tener muchos seguidores y un Usuario puede seguir a muchos Usuarios.
    seguidores = models.ManyToManyField('Usuario', related_name='seguidores', blank=True)



# Tabla: Historial de reproducción
class Historial_reproduccion(models.Model):
    # Campo de ID que se autoincrementa.
    id_hostorial_reproduccion = models.AutoField(primary_key=True)
    # Relación muchos a uno con Usuario. Si se elimina un Usuario, se eliminan las entradas de su Historial de Reproducción.
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # Relación muchos a uno con Cancion. Si se elimina una Cancion, se eliminan las entradas de su Historial de Reproducción.
    id_cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    # Campo para la fecha de reproducción. Se establece automáticamente al crear la entrada en el Historial de Reproducción.
    fecha_reproduccion = models.DateTimeField(auto_now_add=True)
    # Campo para la búsqueda reciente del usuario. Puede ser NULL o estar en blanco.
    busqueda_reciente = models.CharField(max_length=255, null=True, blank=True)


# Tabla: Artista favorito
class Artista_favorito(models.Model):
    # Campo de ID que se autoincrementa.
    id_artista_favorito = models.AutoField(primary_key=True)
    # Relación muchos a uno con Usuario. Si se elimina un Usuario, se eliminan sus Artistas Favoritos.
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # Relación muchos a uno con Artista. Si se elimina un Artista, se eliminan las entradas de Artistas Favoritos.
    id_artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    # Campo para el género musical. Puede ser NULL.
    genero = models.CharField(max_length=255, null=True, blank=True)


# Tarea que usa cada uno
# Avanzar con 7 clases con atributos y tipos de datos