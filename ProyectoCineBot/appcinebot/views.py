from django.http import HttpResponse
from django.shortcuts import render
from .models import Pelicula, Genero


# Create your views here.

def index(request):
    try:
        peliculas = Pelicula.objects.all()
        generos = Genero.objects.all()
        context= {'peliculas':peliculas,'generos':generos}
        return render(request, "index.html", context)
    except:
        mensaje = "Problemas de carga en el home."
        return HttpResponse(mensaje)


def list(request):
  imagen = Pelicula.objects.all()
  return render(request, "index.html", {'imagen': imagen})

def buscar(request):

    generos = Genero.objects.all()

    try:
        if request.GET["txt_pelicula"]:
            try:
                if request.GET["exampleRadios"]:
                    genero = request.GET["exampleRadios"]
                    pelicula = request.GET["txt_pelicula"]
                    peliculas = Pelicula.objects.filter(nombre__icontains=pelicula,genero__icontains=genero)
                    context= {'peliculas':peliculas,"query":pelicula,'generos':generos}
                    return render(request,"searchmovie.html",context)
            except:
                pelicula = request.GET["txt_pelicula"]
                peliculas = Pelicula.objects.filter(nombre__icontains=pelicula)
                context= {'peliculas':peliculas,"query":pelicula,'generos':generos}
                return render(request,"searchmovie.html",context)
        
        else:
            mensaje = "Debe ingresar nombre de la pelicula"
            return HttpResponse(mensaje)
    except:
        mensaje = "Debe ingresar nombre de la pelicula"
        return HttpResponse(mensaje)



def vistaporgeneros(request):

    try:
        peliculas = Pelicula.objects.all()
        generos = Genero.objects.all()
        generoEscogido = request.GET["generoElegido"]
        context= {'peliculas':peliculas,'generos':generos,'generoEscogido':generoEscogido}
        return render(request, "vgenero.html", context)
    except:
        mensaje = "Problemas de carga en la vista por generos."
        return HttpResponse(mensaje)















