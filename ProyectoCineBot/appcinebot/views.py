
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

















