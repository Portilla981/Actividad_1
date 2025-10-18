from django.db import models

# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField()

class Medico(models.Model):
    numero_licencia = models.CharField(max_length=25)
    horario_inicio = models.TimeField()
    horario_fin = models.TimeField()
