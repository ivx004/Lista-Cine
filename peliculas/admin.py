from django.contrib import admin
from .models import Pelicula


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "genero", "creada")
    list_filter = ("genero",)
    search_fields = ("titulo", "genero")
    ordering = ("-creada",)
