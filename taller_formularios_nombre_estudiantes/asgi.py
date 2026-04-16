import os

from django.core.asgi import get_asgi_application


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "taller_formularios_nombre_estudiantes.settings"
)

application = get_asgi_application()