from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Reserva.

    Este serializador se utiliza para:
    - Convertir instancias del modelo Reserva en representaciones JSON (serialización).
    - Validar y deserializar datos JSON enviados desde clientes hacia objetos del modelo Reserva.
    
    La clase Meta especifica las configuraciones del serializador.
    """
    class Meta:
        model = Reserva
        fields = '__all__'
