"""
URL configuration for psicologia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core.views import InicioView
from core.views import Custom403View

handler403 = Custom403View.as_view()

# Definir el esquema para la documentación de Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API de Reservas",
      default_version='v1',
      description="Documentación para la API de gestión de reservas",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@reservas.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioView.as_view(), name='inicio'),
    path('', include('core.urls')),
    path('api/', include('core.urls')),  
    path('swagger/', schema_view.as_view(), name='swagger-docs'),
   
]
