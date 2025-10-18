from django.db import models

# Create your models here.
class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField()


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    fecha_ingreso = models.DateField()