from django.db import models

# Create your models here.
class Socio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    nombreUsuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=128)