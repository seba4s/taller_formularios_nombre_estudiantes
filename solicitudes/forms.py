from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    """
    Formulario para la creación y edición de solicitudes.
    
    Utiliza todos los campos del modelo Solicitud y proporciona validaciones
    automáticas basadas en los tipos de campo definidos en el modelo.
    """
    
    class Meta:
        model = Solicitud
        fields = [
            'nombre_solicitante',
            'documento_identidad',
            'correo_electronico',
            'telefono_contacto',
            'tipo_solicitud',
            'asunto',
            'descripcion_detallada',
            'archivo_adjunto',
        ]
        
        widgets = {
            'nombre_solicitante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa tu nombre completo',
                'required': True,
            }),
            'documento_identidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 1234567890',
                'required': True,
            }),
            'correo_electronico': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu.email@ejemplo.com',
                'required': True,
            }),
            'telefono_contacto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: +34 666 777 888',
                'required': True,
            }),
            'tipo_solicitud': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Resumen breve del asunto',
                'required': True,
            }),
            'descripcion_detallada': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe en detalle tu solicitud...',
                'rows': 6,
                'required': True,
            }),
            'archivo_adjunto': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx,.txt,.jpg,.png,.jpeg',
            }),
        }
    
    def clean_documento_identidad(self):
        """Valida que el documento de identidad no esté vacío."""
        documento = self.cleaned_data.get('documento_identidad')
        if documento:
            documento = documento.strip()
            if not documento:
                raise forms.ValidationError('El documento de identidad no puede estar vacío.')
        return documento
    
    def clean_asunto(self):
        """Valida que el asunto tenga al menos 5 caracteres."""
        asunto = self.cleaned_data.get('asunto')
        if asunto and len(asunto.strip()) < 5:
            raise forms.ValidationError('El asunto debe tener al menos 5 caracteres.')
        return asunto
    
    def clean_descripcion_detallada(self):
        """Valida que la descripción tenga al menos 10 caracteres."""
        descripcion = self.cleaned_data.get('descripcion_detallada')
        if descripcion and len(descripcion.strip()) < 10:
            raise forms.ValidationError('La descripción debe tener al menos 10 caracteres.')
        return descripcion
