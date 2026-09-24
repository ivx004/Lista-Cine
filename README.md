# Lista Cine — proyecto Django

Aplicación web para administrar una lista de películas. Cumple la actividad de Django ORM, formularios, operaciones CRUD y Django Admin.

## Funcionalidades

- Modelo `Pelicula` con título, género y fecha de registro.
- Formulario con dos campos y botón para agregar películas.
- Lista visible de películas guardadas.
- Botón para borrar cada película (con protección CSRF).
- Modelo registrado en Django Admin con búsqueda y filtros.
- Migración inicial incluida.

## Ejecutar localmente

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abre `http://127.0.0.1:8000/`. Para usar el panel administrativo:

```bash
python manage.py createsuperuser
```

Luego visita `http://127.0.0.1:8000/admin/`.
