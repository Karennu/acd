"""arteycultura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from arteycultura.views import inicio, enviarCorreo, ingresar, registraUsuario, salir
from registro.views import registro, ListaRegistros 
from arte.views import agregar as addArte, inicio as startA, ListaActividades
from deportes.views import agregarDeporte as addDeporte, inicio as startD, ListaActividades as ListaActividadesDeportes

urlpatterns = [
path('admin/', admin.site.urls),
    url(r"registro$", ListaRegistros.as_view()),
    url(r"registro/add$", registro),
    url(r"^$", inicio),
    url(r"^arte/add$", addArte),
    url(r"^deportes/add$", addDeporte),
    url(r"arte$", ListaActividades.as_view()),
    url(r"deporte$", ListaActividadesDeportes.as_view()),
    url(r"correo$", enviarCorreo),
    url(r"^login$", ingresar),
    url(r"^logout$", salir),
    url(r"usuario/agregar$", registraUsuario),
]
