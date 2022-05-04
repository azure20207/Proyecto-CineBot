
from django.db import models

# Create your models here.

class Pelicula(models.Model):
    nombre=models.CharField(max_length=50)
    sinopsis=models.CharField(max_length=200)
    año=models.CharField(max_length=50)
    genero=models.CharField(max_length=50)
    actores=models.CharField(max_length=50)
    puntuacion=models.CharField(max_length=50)
    visualizacion=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="peliculas", null=True)

    
