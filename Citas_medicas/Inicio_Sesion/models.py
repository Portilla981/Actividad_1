from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id_usuario = models.CharField(max_length = 20)
    nombres_usuario = models.CharField(max_length = 30)
    apellidos_usuarios = models.CharField(max_length=30)
    telefono_usuario = models.CharField(max_length = 15)
    direccion_usuario = models.CharField(max_length = 100)
    fecha_nacimiento = models.DateField()

# Proceso de creacion de tipos de usuario o perfiles
class Tipo_Usuario(models.Model):
    id_tipo_usuario = models.IntegerField()
    nombre_tipo_usuario = models.CharField(max_length=10)

