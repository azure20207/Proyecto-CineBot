from django.contrib import admin

# Register your models here.

from appcinebot.models import Pelicula, Genero
admin.site.register(Pelicula)
admin.site.register(Genero)
