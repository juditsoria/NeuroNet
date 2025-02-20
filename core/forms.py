from django import forms
from .models import Reserva, Usuario
from django.contrib.auth.forms import UserCreationForm

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_cliente', 'fecha_reserva', 'email_cliente', 'telefono_cliente', 'servicio']
        exclude = ['cliente']
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Ingrese su nombre"
            }),
            'fecha_reserva': forms.DateInput(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Seleccione la fecha",
                "type": "date"  # O "datetime-local", según necesites
            }),
            'email_cliente': forms.EmailInput(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Ingrese su correo electrónico"
            }),
            'telefono_cliente': forms.TextInput(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Ingrese su teléfono"
            }),
            'servicio': forms.Select(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            }),
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={
            "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Ingrese su usuario"
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Ingrese su contraseña"
        })
    )

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    perfil = forms.ChoiceField(
        choices=Usuario.PERFILES,
        widget=forms.Select(attrs={
            "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        })
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'perfil', 'password1', 'password2']
        widgets = {
            'nombre': forms.TextInput(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Ingrese su nombre",
                "style": "color: black;"
            }),
            'email': forms.EmailInput(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Ingrese su correo electrónico",
                "style": "color: black;" 
            }),
            'password1': forms.PasswordInput(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Ingrese su contraseña",
                "style": "color: black;" 
            }),
            'password2': forms.PasswordInput(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Confirme su contraseña",
                "style": "color: black;"
            }),
        }
