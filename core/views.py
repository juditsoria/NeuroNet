from django.shortcuts import render
from .models import Service, Reserva, Categoria, Recurso
from django.views.generic import ListView
from .serializers import ReservaSerializer
from rest_framework import generics
from .forms import ReservaForm
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic import TemplateView
from .datos_api import obtener_datos



def home(request):
    return render(request, 'home.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'lista_reservas.html', {'reservas': reservas})

class ReservaList(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    
class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'crear_reserva.html'  
    success_url = '/crear_reserva/'

    def form_valid(self, form):
        messages.success(self.request, "Tu reserva ha sido realizada correctamente.")
        return super().form_valid(form)


class RecursoListView(ListView):
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


class FuentesConfiablesView(TemplateView):
    template_name = "fuentes_confiables.html"
    
class DatosApiView(TemplateView):
    template_name = 'datos.html'

    def get_context_data(self, **kwargs):
        # Llamamos a la función que obtiene los datos de la API
        context = super().get_context_data(**kwargs)
        context['articulos'] = obtener_datos()  # Los artículos obtenidos de la API
        return context