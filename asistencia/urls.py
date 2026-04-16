from django.urls import path

from .views import confirmacion_asistencia, registro_asistencia


urlpatterns = [
    path("registro/", registro_asistencia, name="registro_asistencia"),
    path("confirmacion/", confirmacion_asistencia, name="confirmacion_asistencia"),
]