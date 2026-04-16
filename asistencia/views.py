from django.shortcuts import get_object_or_404, redirect, render

from .forms import AsistenciaForm
from .models import Asistencia


def registro_asistencia(request):
    if request.method == "POST":
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            asistencia = form.save()
            request.session["ultima_asistencia_id"] = asistencia.pk
            return redirect("confirmacion_asistencia")
    else:
        form = AsistenciaForm()

    return render(
        request,
        "asistencia/formulario_asistencia.html",
        {"form": form},
    )


def confirmacion_asistencia(request):
    asistencia_id = request.session.get("ultima_asistencia_id")
    asistencia = None

    if asistencia_id is not None:
        asistencia = get_object_or_404(Asistencia, pk=asistencia_id)

    return render(
        request,
        "asistencia/confirmacion_asistencia.html",
        {"asistencia": asistencia},
    )