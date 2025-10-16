# api/serializers.py
from rest_framework import serializers
from .models import Conductor, Ruta

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__' # Incluye todos los campos del modelo

class RutaSerializer(serializers.ModelSerializer):
    # ✨ PUNTO EXTRA: Personalización para mostrar el nombre del conductor
    # en lugar de solo su ID.
    nombre_conductor = serializers.CharField(source='conductor.nombre', read_only=True)

    class Meta:
        model = Ruta
        # Agregamos 'nombre_conductor' a la lista de campos a mostrar.
        fields = ['id', 'origen', 'destino', 'horario', 'conductor', 'nombre_conductor']
        # Hacemos que 'conductor' (el ID) sea de solo escritura,
        # ya que solo lo necesitamos para crear/actualizar la relación.
        extra_kwargs = {
            'conductor': {'write_only': True}
        }