from django.db import models


class Pelicula(models.Model):
    titulo = models.CharField("título", max_length=150)
    genero = models.CharField("género", max_length=80)
    creada = models.DateTimeField("fecha de registro", auto_now_add=True)

    class Meta:
        ordering = ["-creada"]
        verbose_name = "película"
        verbose_name_plural = "películas"

    def __str__(self):
        return f"{self.titulo} ({self.genero})"
