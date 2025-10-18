from django.db import models

# Create your models here.
class Recepcionista(models.Model):
    turno = models.CharField(max_length=20)

class gestionCita(models.Model):
    ingreso_paciente = models.BooleanField(default=False)
    cancelacion_cita = models.BooleanField(default=False)
    motivo_cancelacion = models.CharField()
