from django.urls import path
from . import views

app_name = "peliculas"

urlpatterns = [
    path("", views.lista_peliculas, name="lista"),
    path("agregar/", views.agregar_pelicula, name="agregar"),
    path("eliminar/<int:pk>/", views.eliminar_pelicula, name="eliminar"),
]
