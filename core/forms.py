from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_cliente', 'fecha_reserva', 'email_cliente', 'telefono_cliente', 'servicio']
