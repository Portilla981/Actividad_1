from django.db import models

# Create your models here.
class Triage(models.Model):
    nivel_prioridad = models.IntegerField()
    fecha_evaluacion = models.DateTimeField()
    observaciones = models.CharField()

class SignosVitales(models.Model):
    presion_arterial = models.CharField(max_length=10)
    frecuencia_cardiaca = models.IntegerField()
    frecuencia_respiratoria = models.IntegerField()
    saturacion_oxigeno = models.IntegerField()