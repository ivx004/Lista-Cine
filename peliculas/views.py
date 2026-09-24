from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PeliculaForm
from .models import Pelicula


def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    form = PeliculaForm()
    return render(request, "peliculas/lista.html", {"peliculas": peliculas, "form": form})


def agregar_pelicula(request):
    if request.method != "POST":
        return redirect("peliculas:lista")

    form = PeliculaForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "La película se agregó a tu lista.")
    return redirect("peliculas:lista")


def eliminar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == "POST":
        pelicula.delete()
        messages.success(request, "La película se eliminó de tu lista.")
    return redirect("peliculas:lista")
