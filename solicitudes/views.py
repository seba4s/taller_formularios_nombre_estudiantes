from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .forms import SolicitudForm
from .models import Solicitud


@require_http_methods(['GET', 'POST'])
def registro_solicitud(request):
    """
    Vista para registrar una nueva solicitud.
    
    GET: Muestra el formulario vacío para crear una solicitud.
    POST: Procesa el formulario, valida los datos, guarda la solicitud
          (incluyendo archivo si se proporcionó) y redirige a confirmación.
    """
    
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Guardar la solicitud en la base de datos
            solicitud = form.save()
            
            # Mensaje de éxito
            messages.success(
                request,
                f'¡Solicitud registrada correctamente! ID: {solicitud.id}'
            )
            
            # Redirigir a la página de confirmación
            return redirect('solicitudes:confirmacion_solicitud')
        else:
            # Mensaje de error si el formulario no es válido
            messages.error(
                request,
                'Por favor, revisa los errores en el formulario.'
            )
    else:
        # Mostrar formulario vacío en GET
        form = SolicitudForm()
    
    context = {
        'form': form,
        'titulo': 'Registro de Solicitud',
    }
    
    return render(request, 'solicitudes/formulario_solicitud.html', context)


@require_http_methods(['GET'])
def confirmacion_solicitud(request):
    """
    Vista para mostrar la página de confirmación.
    
    Muestra un mensaje de éxito después de registrar una solicitud y
    proporciona un resumen de los datos registrados (última solicitud).
    """
    
    # Obtener la última solicitud registrada para mostrar sus datos
    ultima_solicitud = Solicitud.objects.order_by('-fecha_solicitud').first()
    
    context = {
        'titulo': 'Confirmación de Solicitud',
        'solicitud': ultima_solicitud,
    }
    
    return render(request, 'solicitudes/confirmacion_solicitud.html', context)
