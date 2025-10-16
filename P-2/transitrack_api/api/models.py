from django.db import models


class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    numero_licencia = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Ruta(models.Model):
    origen = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)
    horario = models.TimeField()
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE, related_name='rutas')

    def __str__(self):
        return f'{self.origen} - {self.destino}'
