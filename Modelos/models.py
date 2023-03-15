from django.db import models

class clientes (models.Model):
    mail = models.EmailField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    fecha_registro = models.DateField()

# Create your models here.
