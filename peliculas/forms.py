from django import forms
from .models import Pelicula


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ["titulo", "genero"]
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Ej: El padrino"}),
            "genero": forms.TextInput(attrs={"placeholder": "Ej: Drama"}),
        }
