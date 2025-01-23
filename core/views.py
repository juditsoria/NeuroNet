from django.shortcuts import render
from .models import Service, Reserva, Categoria, Recurso
from .serializers import ReservaSerializer
from rest_framework import generics
from .forms import ReservaForm
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .datos_api import obtener_datos
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class ServicesView(LoginRequiredMixin, ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'


class ListaReservasView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'lista_reservas.html'
    context_object_name = 'lista_reservas'


class ReservaList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    
class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'crear_reserva.html'  
    success_url = '/crear_reserva/'

    def form_valid(self, form):
        messages.success(self.request, "Tu reserva ha sido realizada correctamente.")
        return super().form_valid(form)


class RecursoListView(LoginRequiredMixin, ListView):
    model = Recurso
    template_name = 'recursos.html'
    context_object_name = 'recursos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

    def get_queryset(self):
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            return Recurso.objects.filter(categoria_id=categoria_id)
        return Recurso.objects.all()


class FuentesConfiablesView(LoginRequiredMixin, TemplateView):
    template_name = "fuentes_confiables.html"
    
class DatosApiView(LoginRequiredMixin, TemplateView):
    template_name = 'datos.html'

    def get_context_data(self, **kwargs):
        # Llamamos a la función que obtiene los datos de la API
        context = super().get_context_data(**kwargs)
        context['articulos'] = obtener_datos()  # Los artículos obtenidos de la API
        return context
    
class RegistroUsuarioView(CreateView):
    template_name = 'registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirige al login después del registro
    
    
class LoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
# class LogoutView(LogoutView):
#     template_name = 'core/logout.html'

    
class LandingView(TemplateView):
    template_name = 'landing.html'
    
    
