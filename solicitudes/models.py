from django.db import models


class Solicitud(models.Model):
    """
    Modelo para gestionar solicitudes de estudiantes.
    
    Permite registrar solicitudes académicas, administrativas, técnicas u otras,
    con información del solicitante y documentación adjunta opcional.
    """
    
    TIPO_SOLICITUD_CHOICES = [
        ('academica', 'Académica'),
        ('administrativa', 'Administrativa'),
        ('tecnica', 'Técnica'),
        ('otra', 'Otra'),
    ]
    
    nombre_solicitante = models.CharField(
        max_length=150,
        verbose_name='Nombre del solicitante',
        help_text='Nombre completo de quien realiza la solicitud'
    )
    
    documento_identidad = models.CharField(
        max_length=50,
        verbose_name='Documento de identidad',
        help_text='Cédula, pasaporte u otro documento de identificación'
    )
    
    correo_electronico = models.EmailField(
        verbose_name='Correo electrónico',
        help_text='Correo de contacto válido'
    )
    
    telefono_contacto = models.CharField(
        max_length=20,
        verbose_name='Teléfono de contacto'
    )
    
    tipo_solicitud = models.CharField(
        max_length=20,
        choices=TIPO_SOLICITUD_CHOICES,
        verbose_name='Tipo de solicitud',
        help_text='Selecciona la categoría de tu solicitud'
    )
    
    asunto = models.CharField(
        max_length=200,
        verbose_name='Asunto',
        help_text='Resumen breve del motivo de la solicitud'
    )
    
    descripcion_detallada = models.TextField(
        verbose_name='Descripción detallada',
        help_text='Explica en detalle tu solicitud'
    )
    
    fecha_solicitud = models.DateField(
        verbose_name='Fecha de solicitud',
        auto_now_add=True,
        help_text='Se registra automáticamente la fecha actual'
    )
    
    archivo_adjunto = models.FileField(
        upload_to='adjuntos/',
        blank=True,
        null=True,
        verbose_name='Archivo adjunto',
        help_text='Puedes adjuntar documentos de soporte (opcional)'
    )
    
    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        ordering = ['-fecha_solicitud']
        indexes = [
            models.Index(fields=['-fecha_solicitud']),
            models.Index(fields=['tipo_solicitud']),
        ]
    
    def __str__(self):
        return f"Solicitud {self.tipo_solicitud} - {self.nombre_solicitante} ({self.fecha_solicitud})"
