from django import forms 

from .models import Deporte 

class FormularioDeportes(forms.ModelForm):
    class Meta:
        model = Deporte 

        fields = ["nombre", "descripcion"]