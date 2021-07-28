from django.shortcuts import redirect, render
from registro.formulario import FormularioPersona
from django.core.mail import EmailMessage
from django.http import HttpResponse
from arteycultura.views import enviarCorreo
from .models import Persona
from django.views import generic

# Create your views here.
def registro (request):
    formulario = FormularioPersona()
    if request.method == "POST": 
        formulario = FormularioPersona(request.POST)
        if formulario.is_valid():
            formulario.save()
            #nombre = request.POST["nombre"]
            #correo = request.POST["correo"]
            #enviarCorreo(correo)
            nombre = request.POST["nombre"]
            apellido = request.POST["apellidos"]
            enviarCorreo(request, nombre, apellido)
            return redirect("/")
    return render(request, "registro.html", {"form":formulario})

#def enviarCorreo(correo):
 #   correo = EmailMessage("Prueba de correo", "Hola", to = [correo])
  #  correo.send()
   # return HttpResponse("hola")

class ListaRegistros(generic.ListView):
    model = Persona
    context_object_name = "personasRegistradas"
    template_name = "registro.html"