from django.urls import path
from . import views
from .views import ReservaDetail, ReservaCreateView, RecursoListView, FuentesConfiablesView, DatosApiView


urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('crear_reserva/', ReservaCreateView.as_view(), name='crear_reserva'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/<int:pk>/', ReservaDetail.as_view(), name='reserva-detail'),
    path('recursos/', RecursoListView.as_view(), name='recursos_list'),
    path('fuentes_confiables/', FuentesConfiablesView.as_view(), name='fuentes_confiables'),
    path('datos_api/', DatosApiView.as_view(), name='datos_api'),
]
