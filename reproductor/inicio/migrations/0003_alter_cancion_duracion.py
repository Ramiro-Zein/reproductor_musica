# Generated by Django 5.0.2 on 2024-02-28 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_album_ano_lanzamiento_alter_album_artista_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='duracion',
            field=models.CharField(default='', max_length=255),
        ),
    ]