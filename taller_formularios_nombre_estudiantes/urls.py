from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(url="/asistencia/registro/", permanent=False)),
    path("admin/", admin.site.urls),
    path("asistencia/", include("asistencia.urls")),
    path("solicitudes/", include("solicitudes.urls")),
]