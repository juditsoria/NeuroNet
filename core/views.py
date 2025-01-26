from django.shortcuts import render
from .models import Service, Reserva, Categoria, Recurso
from .serializers import ReservaSerializer
from rest_framework import generics
from .forms import ReservaForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .datos_api import obtener_datos
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django import forms
from .models import Usuario  
from django.core.exceptions import PermissionDenied
from django.views import View


class HomeView(LoginRequiredMixin, TemplateView):
    '''
    Muestra la página principal del usuario autenticado (home.html). 
    Redirige a la landing page si el usuario no está autenticado.
    '''
    template_name = 'home.html'
    
    def dispatch(self, request, *args, **kwargs):
        '''
    - dispatch(request, *args, **kwargs): Verifica si el usuario está autenticado. 
      Si está autenticado, muestra la página principal (home.html); de lo contrario, redirige a la página de aterrizaje (landing.html).
    '''
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('landing') 


class ServicesView(LoginRequiredMixin, ListView):
    '''
    Muestra la lista de servicios disponibles (services.html). 
    Utiliza el modelo Service para obtener los datos.
    - context_object_name: Define el nombre del contexto ('services') que se usará en la plantilla (services.html).
    - model: Utiliza el modelo Service para extraer la información de los servicios disponibles.
    '''
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'


class ListaReservasView(LoginRequiredMixin, ListView):
    '''
    Muestra la lista de reservas realizadas por los usuarios (lista_reservas.html). 
    Utiliza el modelo Reserva para obtener los datos.
     - context_object_name: Define el nombre del contexto ('lista_reservas') para acceder a las reservas desde la plantilla (lista_reservas.html).
    - model: Utiliza el modelo Reserva para obtener los datos.
    '''
    model = Reserva
    template_name = 'lista_reservas.html'
    context_object_name = 'lista_reservas'

    def get_queryset(self):
        """
        Filtra las reservas según el perfil del usuario.
        """
        usuario_actual = self.request.user
        if usuario_actual.perfil == 'psicologo':
            return Reserva.objects.all()  # Los psicólogos ven todas las reservas
        return Reserva.objects.filter(cliente=usuario_actual)  # Los clientes ven sus propias reservas

class ReservaList(LoginRequiredMixin, generics.ListCreateAPIView):
    '''
    APIView para listar y crear nuevas reservas. 
    Utiliza el modelo Reserva y el serializer ReservaSerializer.
    - queryset: Recupera todas las reservas del modelo Reserva.
    - serializer_class: Asocia el serializer ReservaSerializer para gestionar la transformación de datos entre JSON y objetos del modelo.
    '''
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    '''
    APIView para recuperar, actualizar o eliminar una reserva específica. 
    Utiliza el modelo Reserva y el serializer ReservaSerializer.
     - queryset: Recupera una reserva específica basada en su ID.
    - serializer_class: Asocia el serializer ReservaSerializer para permitir la lectura, modificación o eliminación de una reserva.
    '''
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    
class ReservaCreateView(LoginRequiredMixin, CreateView):
    '''
    Formulario para crear una nueva reserva (crear_reserva.html). 
    Al enviar el formulario exitosamente, redirige al mismo formulario y muestra un mensaje de éxito.
    Utiliza el modelo Reserva y el formulario ReservaForm.
    '''
    model = Reserva
    form_class = ReservaForm
    template_name = 'crear_reserva.html'
    success_url = reverse_lazy('lista_reservas')

    def dispatch(self, request, *args, **kwargs):
        """
        Restringe la creación de reservas solo a usuarios con perfil 'cliente'.
        """
        if request.user.perfil != 'cliente':
            raise PermissionDenied("No tienes permiso para crear una reserva. Debes tener el perfil de cliente.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Asigna automáticamente el cliente actual a la reserva.
        """
        form.instance.cliente = self.request.user  # Asigna el cliente actual
        messages.success(self.request, "Tu reserva ha sido realizada correctamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Muestra un mensaje de error si el formulario no es válido.
        """
        messages.error(self.request, "Hubo un error al crear la reserva. Por favor, revisa los datos.")
        return super().form_invalid(form)

class ReservaUpdateView(LoginRequiredMixin, UpdateView):
    '''
    Vista para editar una reserva existente.

    Esta vista permite a los usuarios autenticados (clientes y psicólogos) 
    editar una reserva. Dependiendo del tipo de usuario (cliente o psicólogo), 
    se aplican filtros diferentes para determinar qué reservas pueden ser editadas.

    Atributos:
        model (Reserva): El modelo de la reserva que se va a editar.
        fields (list): Los campos del modelo que se pueden editar.
        template_name (str): La plantilla utilizada para renderizar el formulario de edición.
        success_url (str): La URL a la que se redirige después de una edición exitosa.

    Métodos:
        get_queryset: Filtra las reservas que el usuario puede editar según su rol.
    '''
    model = Reserva
    fields = ['fecha_reserva', 'servicio', 'comentarios']  
    template_name = "editar_reserva.html"
    success_url = reverse_lazy('lista_reservas')

    def get_queryset(self):
        """
        Permite que tanto el cliente como los psicólogos editen la reserva.
        """
        usuario_actual = self.request.user
        if usuario_actual.perfil == 'psicologo':
            return Reserva.objects.all()  
        return Reserva.objects.filter(cliente=usuario_actual)  
    
class ReservaDeleteView(LoginRequiredMixin, DeleteView):
    '''
    Vista para eliminar una reserva existente.

    Esta vista permite a los usuarios autenticados (clientes y psicólogos) 
    eliminar una reserva. Dependiendo del tipo de usuario (cliente o psicólogo), 
    se aplican filtros diferentes para determinar qué reservas pueden ser eliminadas.

    Atributos:
        model (Reserva): El modelo de la reserva que se va a eliminar.
        template_name (str): La plantilla utilizada para renderizar la confirmación de eliminación.
        success_url (str): La URL a la que se redirige después de una eliminación exitosa.

    Métodos:
        get_queryset: Filtra las reservas que el usuario puede eliminar según su rol.
    '''
    model = Reserva
    template_name = "eliminar_reserva.html"
    success_url = reverse_lazy('lista_reservas')

    def get_queryset(self):
        """
        Permite que tanto el cliente como los psicólogos eliminen la reserva.
        """
        usuario_actual = self.request.user
        if usuario_actual.perfil == 'psicologo':
            return Reserva.objects.all()  
        return Reserva.objects.filter(cliente=usuario_actual)  

    
class RecursoListView(LoginRequiredMixin, ListView):
    '''
    Muestra la lista de recursos disponibles (recursos.html), 
    con la posibilidad de filtrar por categorías. 
    Utiliza el modelo Recurso y añade las categorías al contexto.
     - model: Utiliza el modelo Recurso para obtener los datos.
    - template_name: Renderiza la plantilla recursos.html.
    - context_object_name: Define el nombre del contexto ('recursos') para usarlo en la plantilla (recursos.html).
    '''
    model = Recurso
    template_name = 'recursos.html'
    context_object_name = 'recursos'

    def get_context_data(self, **kwargs):
        '''
        - get_context_data(**kwargs): Añade al contexto una lista de categorías del modelo Categoria para filtrar recursos.
        '''
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

    def get_queryset(self):
        '''
        - get_queryset(): Recupera los recursos filtrados por categoría (si se selecciona) o todos los recursos si no hay filtro.
        '''
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            return Recurso.objects.filter(categoria_id=categoria_id)
        return Recurso.objects.all()


class FuentesConfiablesView(LoginRequiredMixin, TemplateView):
    '''
    Muestra una página con información sobre fuentes confiables (fuentes_confiables.html).
     - template_name: Renderiza la plantilla fuentes_confiables.html, que contiene información estática sobre fuentes confiables.
    '''
    template_name = "fuentes_confiables.html"
    
class DatosApiView(LoginRequiredMixin, TemplateView):
    '''
    Muestra una página que consume datos de una API externa y los presenta en formato de artículos (datos.html).
    Los datos son obtenidos mediante la función obtener_datos.
    - template_name: Renderiza la plantilla datos_api.html.
    '''
    template_name = 'datos.html'

    def get_context_data(self, **kwargs):
        '''
        - get_context_data(**kwargs): Recupera datos desde una API externa mediante la función obtener_datos y los añade al contexto como 'articulos'.
        '''
        context = super().get_context_data(**kwargs)
        context['articulos'] = obtener_datos()  
        return context
    


class RegistroUsuarioForm(UserCreationForm):
    """
    Extiende el formulario de registro para incluir un campo de perfil (psicólogo o cliente).
    """
    PERFILES = (
        ('psicologo', 'Psicólogo'),
        ('cliente', 'Cliente'),
    )
    perfil = forms.ChoiceField(choices=PERFILES, required=True, label="Tipo de Perfil")

    class Meta:
        model = Usuario  # Usa tu modelo personalizado
        fields = ['nombre', 'email', 'perfil', 'password1', 'password2']

class RegistroUsuarioView(CreateView):
    """
    Permite a los usuarios registrarse en el sistema con selección de perfil.
    """
    template_name = 'registro.html'
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """
        Si el formulario es válido, guarda al usuario y muestra un mensaje de éxito.
        """
        user = form.save() 
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Si el formulario tiene errores, muestra un mensaje de error.
        """
        print(form.errors) 
        messages.error(
            self.request, 
            "Hubo un error al intentar registrarte. Por favor, revisa los campos. "
            "La contraseña debe tener al menos 8 caracteres."
        )
        return super().form_invalid(form)

    
class LoginView(LoginView):
    '''
    Muestra el formulario de inicio de sesión (login.html). 
    Redirige al home tras un inicio exitoso. 
    Muestra mensajes de error si las credenciales son incorrectas.
    - template_name: Renderiza la plantilla login.html.
    '''
    template_name = 'login.html'

    def get_success_url(self):
        '''
        - get_success_url(): Redirige al usuario a la página principal (home.html) tras un inicio de sesión exitoso.
        '''
        return reverse_lazy('home')
    
    def form_invalid(self, form):
        '''
        - form_invalid(form): Muestra un mensaje de error si las credenciales ingresadas son incorrectas.
        '''
        messages.error(self.request, "Usuario o contraseña incorrectos.")
        return super().form_invalid(form)
    
class CustomLogoutView(LogoutView):
    '''
    Gestiona el cierre de sesión del usuario. 
    Redirige a la página de aterrizaje (landing.html) tras el cierre de sesión.
    '''
    def get_next_page(self):
        '''
        - get_next_page(): Define la página de aterrizaje (landing.html) como destino tras el cierre de sesión.
        '''
        return 'landing/'


    
class LandingView(TemplateView):
    '''
    Muestra la página de aterrizaje para usuarios no autenticados (landing.html).
    - template_name: Renderiza la plantilla landing.html.
    '''
    template_name = 'landing.html'
    
class Custom403View(TemplateView):
    ''' 
    Muestra un mensaje mas amigable para el usuario para las páginas que estan restringidas.
    - template_name: Renderiza la plantilla 403.html.
    '''
    template_name = '403.html'

    def get(self, request, *args, **kwargs):
        """Define el método HTTP para manejar el error."""
        response = super().get(request, *args, **kwargs)
        response.status_code = 403
        return response
    
    
class InicioView(View):
    '''
    Vista principal que decide a dónde redirigir al usuario al acceder a la raíz del sitio.

    Esta vista verifica si el usuario está autenticado:
    - Si el usuario está autenticado, lo redirige a la página de inicio (home).
    - Si el usuario no está autenticado, lo redirige a la landing page.

    Métodos:
        get: Maneja las solicitudes GET y decide la redirección según el estado de autenticación.
    '''
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Si el usuario está autenticado, redirigir al home
            return redirect('home')
        else:
            # Si el usuario no está autenticado, mostrar la landing page
            return redirect('landing')