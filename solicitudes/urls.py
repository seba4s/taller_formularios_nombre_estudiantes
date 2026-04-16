from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='solicitudes:registro_solicitud', permanent=False)),
    path('registro/', views.registro_solicitud, name='registro_solicitud'),
    path('confirmacion/', views.confirmacion_solicitud, name='confirmacion_solicitud'),
]
