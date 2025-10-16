# api/views.py
from rest_framework import viewsets, filters
from .models import Conductor, Ruta
from .serializers import ConductorSerializer, RutaSerializer

# 뷰셋 para Conductores (CRUD Básico)
class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer

# 뷰셋 para Rutas (CRUD + Búsqueda)
class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

    # 🔍 Funcionalidad de Búsqueda
    filter_backends = [filters.SearchFilter]
    # Definimos los campos por los cuales se puede buscar
    search_fields = ['origen', 'destino']