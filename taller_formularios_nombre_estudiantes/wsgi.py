import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "taller_formularios_nombre_estudiantes.settings"
)

application = get_wsgi_application()