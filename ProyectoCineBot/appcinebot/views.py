from django.http import HttpResponse
from django.shortcuts import render
from .models import Pelicula



# Create your views here.

def index(request):
    peliculas = Pelicula.objects.all()
    context= {'peliculas':peliculas}
    return render(request, "index.html", context)

def list(request):
  imagen = Pelicula.objects.all()
  return render(request, "index.html", {'imagen': imagen})

def buscar(request):
    if request.GET["txt_pelicula"]:
        pelicula = request.GET["txt_pelicula"]
        peliculas = Pelicula.objects.filter(nombre__icontains=pelicula)
        return render(request,"searchmovie.html",{"peliculas":peliculas,"query":pelicula})
    else:
        mensaje = "Debe ingresar nombre de la pelicula"
        return HttpResponse(mensaje)

















