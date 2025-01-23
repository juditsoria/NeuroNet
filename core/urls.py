from django.urls import path
from . import views
from .views import ReservaDetail, ReservaCreateView, RecursoListView, FuentesConfiablesView, DatosApiView, LoginView, LogoutView, RegistroUsuarioView, LandingView, HomeView, ServicesView, ListaReservasView






urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('services/', ServicesView.as_view(), name='services'),
    path('crear_reserva/', ReservaCreateView.as_view(), name='crear_reserva'),
    path('lista_reservas/', ListaReservasView.as_view(), name='lista_reservas'),
    path('reservas/<int:pk>/', ReservaDetail.as_view(), name='reserva-detail'),
    path('recursos/', RecursoListView.as_view(), name='recursos_list'),
    path('fuentes_confiables/', FuentesConfiablesView.as_view(), name='fuentes_confiables'),
    path('datos_api/', DatosApiView.as_view(), name='datos_api'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('landing/', LandingView.as_view(), name='landing'),
]