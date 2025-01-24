from django import forms
from .models import Reserva
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class ReservaForm(forms.ModelForm):
    '''
    Formulario para crear y editar instancias del modelo Reserva.
    Campos:
        - nombre_cliente: Campo para el nombre del cliente que realiza la reserva.
        - fecha_reserva: Campo para seleccionar la fecha y hora de la reserva.
        - email_cliente: Campo para ingresar el correo electrónico del cliente.
        - telefono_cliente: Campo para ingresar el número de teléfono del cliente.
        - servicio: Campo para especificar el servicio asociado a la reserva.
    '''
    class Meta:
        model = Reserva
        fields = ['nombre_cliente', 'fecha_reserva', 'email_cliente', 'telefono_cliente', 'servicio']

class LoginForm(forms.Form):
    '''
    Formulario personalizado para el inicio de sesión.
    Campos:
        - username: Nombre de usuario del cliente. Incluye un widget con estilos Bootstrap.
        - password: Contraseña del cliente. Incluye un widget con estilos Bootstrap y enmascara la entrada.
    '''
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese su usuario"})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Ingrese su contraseña"})
    )

class RegistroForm(UserCreationForm):
    """
    Formulario personalizado para registrar nuevos usuarios con selección de perfil.

    Atributos:
        perfil: Campo ChoiceField que permite seleccionar entre las opciones de perfiles
                definidas en el modelo Usuario.
    
    Meta:
        model: Indica que el modelo asociado al formulario es el modelo Usuario.
        fields: Define los campos que se mostrarán en el formulario, incluyendo:
            - nombre: Nombre del usuario.
            - email: Dirección de correo electrónico del usuario.
            - perfil: Perfil asociado al usuario (por ejemplo, administrador, cliente, etc.).
            - password1: Contraseña.
            - password2: Confirmación de la contraseña.
    """
    perfil = forms.ChoiceField(choices=Usuario.PERFILES)

    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'perfil', 'password1', 'password2']
        


