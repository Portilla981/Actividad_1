from django.db import models

# Create your models here.
class Paciente(models.Model):
    eps = models.CharField(max_length=25)
    tipo_sangre = models.CharField(max_length=2)

class HistorialMedico(models.Model):
    fecha_registro = models.DateField()
    diagnostico = models.CharField()
    tratamiento = models.CharField()
    observaciones = models.CharField()
