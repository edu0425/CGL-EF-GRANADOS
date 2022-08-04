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