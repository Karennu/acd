from django.db import models

class Persona (models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    sexo = models.CharField(max_length=2, choices=[("H", "Hombre"), ("M", "Mujer")])
    correo = models.CharField(max_length=100)

# Create your models here.
