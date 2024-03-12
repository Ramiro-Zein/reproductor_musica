# Generated by Django 5.0.2 on 2024-03-08 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_delete_cancionesplaylist_delete_playlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id_playlist', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default=True, max_length=255)),
                ('descripcion', models.TextField(default='')),
                ('imagen', models.CharField(default=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default=True, max_length=255)),
                ('correo', models.CharField(default=True, max_length=255)),
                ('password', models.CharField(default=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CancionesPlaylist',
            fields=[
                ('id_CancionesPlaylist', models.AutoField(primary_key=True, serialize=False)),
                ('id_cancion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.cancion')),
                ('id_playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.playlist')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.usuario'),
        ),
    ]
