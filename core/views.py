from django.shortcuts import render
from .models import Service, Reserva
from .serializers import ReservaSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .forms import ReservaForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages

def home(request):
    return render(request, 'core/home.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'core/services.html', {'services': services})

def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'core/lista_reservas.html', {'reservas': reservas})

class ReservaList(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    
class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'core/crear_reserva.html'
    success_url = '/crear_reserva/'

    def form_valid(self, form):
        messages.success(self.request, "Tu reserva ha sido realizada correctamente.")
        return super().form_valid(form)