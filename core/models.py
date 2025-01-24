from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Manager personalizado para el modelo de usuario.

    Métodos:
        create_user: Crea un usuario regular con un correo electrónico y una contraseña.
            - email: Dirección de correo electrónico del usuario (obligatorio).
            - password: Contraseña del usuario (opcional).
            - extra_fields: Campos adicionales para el usuario.
        create_superuser: Crea un superusuario con privilegios de administrador.
            - email: Dirección de correo electrónico del superusuario.
            - password: Contraseña del superusuario.
            - extra_fields: Campos adicionales para el superusuario.
            - Asegura que 'is_staff' y 'is_superuser' estén configurados como True.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de usuario personalizado.

    Atributos:
        nombre: Nombre único del usuario (máximo 255 caracteres).
        email: Dirección de correo electrónico única del usuario.
        is_active: Indica si el usuario está activo (por defecto True).
        is_staff: Indica si el usuario tiene acceso al panel de administración (por defecto False).
        perfil: Define el perfil del usuario, con opciones como:
            - Psicólogo
            - Cliente
            - Administrador
        objects: Instancia de UserManager para gestionar la creación de usuarios y superusuarios.
        groups: Relación con los grupos de permisos del usuario, con un `related_name` personalizado 
                para evitar conflictos con otros modelos.
        user_permissions: Relación con los permisos específicos del usuario, también con 
                          un `related_name` personalizado.
        
    Campos personalizados:
        USERNAME_FIELD: Define que el campo principal para autenticación es el 'email'.
        REQUIRED_FIELDS: Campos obligatorios adicionales para crear usuarios ('nombre').

    Métodos:
        __str__: Devuelve la representación en texto del usuario, que en este caso es su email.
    """
    nombre = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    PERFILES = [
        ('psicologo', 'Psicólogo'),
        ('cliente', 'Cliente'),
        ('admin', 'Administrador')
    ]
    perfil = models.CharField(max_length=50, choices=PERFILES, default='admin')

    objects = UserManager()

    groups = models.ManyToManyField(
        Group,
        related_name="usuario_groups",  # Cambia related_name para evitar conflictos
        blank=True,
        verbose_name=_("groups"),
        help_text=_("The groups this user belongs to."),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuario_permissions",  # Cambia related_name para evitar conflictos
        blank=True,
        verbose_name=_("user permissions"),
        help_text=_("Specific permissions for this user."),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.email

class Service(models.Model):
    '''
    Modelo que representa un servicio ofrecido en la plataforma.
    Campos:
        - name: Nombre del servicio (máximo 100 caracteres).
        - description: Descripción detallada del servicio.
        - price: Precio del servicio con hasta 6 dígitos y 2 decimales (e.g., 9999.99).
    '''
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    

class Reserva(models.Model):
    '''
    Modelo que representa una reserva realizada por un cliente.
    Campos:
        - nombre_cliente: Nombre del cliente que realiza la reserva (máximo 100 caracteres).
        - fecha_reserva: Fecha y hora en que se realizará la reserva.
        - email_cliente: Correo electrónico del cliente.
        - telefono_cliente: Teléfono de contacto del cliente (máximo 15 caracteres).
        - servicio: Nombre del servicio asociado con la reserva.
    '''
    nombre_cliente = models.CharField(max_length=100)
    fecha_reserva = models.DateTimeField()
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=15)
    servicio = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Reserva de {self.nombre_cliente} para {self.servicio} el {self.fecha_reserva}"
    
    
class Categoria(models.Model):
    '''
    Modelo que representa una categoría para clasificar recursos.
    Campos:
        - nombre: Nombre de la categoría (máximo 100 caracteres).
    '''
    nombre = models.CharField(max_length=100)

class Recurso(models.Model):
    '''
    Modelo que representa un recurso de aprendizaje (artículo, video o podcast).
    Campos:
        - tipo: Tipo de recurso. Opciones disponibles:
            * 'artículo': Un artículo de texto.
            * 'video': Un video.
            * 'podcast': Un archivo de audio.
        - titulo: Título del recurso (máximo 200 caracteres).
        - categoria: Relación con el modelo Categoria para clasificar recursos.
        - contenido: Contenido principal del recurso.
        - enlace: Un enlace URL asociado con el recurso.
    '''
    tipo = models.CharField(max_length=50, choices=[('artículo', 'Artículo'), ('video', 'Video'), ('podcast', 'Podcast')])
    titulo = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, related_name='recursos', on_delete=models.CASCADE)
    contenido = models.TextField()
    enlace = models.URLField()



