# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConductorViewSet, RutaViewSet

# Creamos un router para registrar nuestras vistas de manera automática
router = DefaultRouter()
router.register(r'conductores', ConductorViewSet, basename='conductor')
router.register(r'rutas', RutaViewSet, basename='ruta')

urlpatterns = [
    path('', include(router.urls)),
]