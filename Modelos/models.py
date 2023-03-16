from django.db import models

class Clientes (models.Model):
    mail = models.EmailField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    fecha_registro = models.DateField()

    class Meta:
        verbose_name_plural = "Clientes"

# Create your models here.
