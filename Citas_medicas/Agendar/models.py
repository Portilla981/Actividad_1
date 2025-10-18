from django.db import models

# Create your models here.
class Agendar_cita(models.Model):
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    especialidad = models.CharField(max_length=50)
    motivo = models.CharField(max_length=50)
    

# Proceso de asignacion de citas
class Asignar_cita(models.Model):
    dia = models.DateField()
    hora_inicio = models.TimeField()
    hora_finalizacion = models.TimeField()

