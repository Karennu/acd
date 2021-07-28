from django.db import models

class Arte(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250, null= True)

# Create your models here.
