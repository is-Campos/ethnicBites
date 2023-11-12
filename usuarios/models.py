from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

# Create your models here.

class Direccion(models.Model):
    nombreCompleto = models.CharField(max_length=150)
    estado= models.CharField(max_length=100)
    ciudad= models.CharField(max_length=100)
    codigoPostal= models.CharField(max_length=5, validators=[MinLengthValidator(limit_value=5)])
    colonia= models.CharField(max_length=100)
    calle= models.CharField(max_length=100)
    numeroExterior= models.CharField(max_length=10)
    numeroInterior= models.CharField(max_length=10, null=True)
    telefono= models.CharField(max_length=10)

class CustomUser(AbstractUser):
    role = models.CharField(max_length=255)
    idDireccion = models.ForeignKey(Direccion,null=True, on_delete=models.SET_NULL)
