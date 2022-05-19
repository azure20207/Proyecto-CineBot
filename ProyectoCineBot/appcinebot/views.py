from django.http import HttpResponse
from django.shortcuts import render
from .models import Pelicula, Genero



# Create your views here.

def index(request):
    peliculas = Pelicula.objects.all()
    generos = Genero.objects.all()
    context= {'peliculas':peliculas,'generos':generos}
    return render(request, "index.html", context)

def list(request):
  imagen = Pelicula.objects.all()
  return render(request, "index.html", {'imagen': imagen})

def buscar(request):

    generos = Genero.objects.all()

    if request.GET[ "exampleRadios"] and request.GET["txt_pelicula"]:
        genero = request.GET["exampleRadios"]
        pelicula = request.GET["txt_pelicula"]
        peliculas = Pelicula.objects.filter(nombre__icontains=pelicula,genero__icontains=genero)
        context= {'peliculas':peliculas,"query":pelicula,'generos':generos}
        return render(request,"searchmovie.html",context)

    elif request.GET["txt_pelicula"]: 
        pelicula = request.GET["txt_pelicula"]
        peliculas = Pelicula.objects.filter(nombre__icontains=pelicula)
        context= {'peliculas':peliculas,"query":pelicula,'generos':generos}
        return render(request,"searchmovie.html",context)
    
    else:
        mensaje = "Debe ingresar nombre de la pelicula"
        return HttpResponse(mensaje)


















