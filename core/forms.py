from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_cliente', 'fecha_reserva', 'email_cliente', 'telefono_cliente', 'servicio']

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese su usuario"})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Ingrese su contraseña"})
    )