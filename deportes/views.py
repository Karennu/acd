from django.shortcuts import render, redirect
from deportes.formulario import FormularioDeportes
from django.http import HttpResponse
from .models import Deporte
from django.views import generic

# Create your views here.

def inicio(request):
    #return HttpResponse("<a href='deportes/add'>Agregar</a>")
    return render(request, "deporte.html")

def agregarDeporte(request):
    f = FormularioDeportes()
    if request.method == "POST":
        f = FormularioDeportes(request.POST)
        if f.is_valid():
            f.save()
            return redirect("/")
    return render(request, "deporte.html",{"form":f})

class ListaActividades(generic.ListView):
    model = Deporte
    context_object_name = "actividadesdeporte"
    template_name = "deporte.html"