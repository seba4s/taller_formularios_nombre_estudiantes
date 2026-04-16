from django import forms

from .models import Asistencia


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = [
            "nombre_completo",
            "documento_identidad",
            "correo_electronico",
            "fecha_asistencia",
            "hora_ingreso",
            "hora_salida",
            "presente",
            "observaciones",
        ]
        widgets = {
            "nombre_completo": forms.TextInput(
                attrs={"placeholder": "Nombre completo del estudiante"}
            ),
            "documento_identidad": forms.TextInput(
                attrs={"placeholder": "Documento de identidad"}
            ),
            "correo_electronico": forms.EmailInput(
                attrs={"placeholder": "correo@ejemplo.com"}
            ),
            "fecha_asistencia": forms.DateInput(attrs={"type": "date"}),
            "hora_ingreso": forms.TimeInput(attrs={"type": "time"}),
            "hora_salida": forms.TimeInput(attrs={"type": "time"}),
            "observaciones": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Observaciones adicionales"}
            ),
        }
        labels = {
            "nombre_completo": "Nombre completo",
            "documento_identidad": "Documento de identidad",
            "correo_electronico": "Correo electronico",
            "fecha_asistencia": "Fecha de asistencia",
            "hora_ingreso": "Hora de ingreso",
            "hora_salida": "Hora de salida",
            "presente": "Presente",
            "observaciones": "Observaciones",
        }