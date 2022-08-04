from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()
    Fecha_compra = models.DateTimeField()
    Fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1)

class Curso(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    horas = models.CharField(max_length=2)
    creditos = models.CharField(max_length=2)
    Fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1)
