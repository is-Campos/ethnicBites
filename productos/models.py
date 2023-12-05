from django.db import models
from django.core.validators import MinValueValidator
from usuarios.models import CustomUser

# Create your models here.

class Producto(models.Model):
      nombre = models.CharField(max_length=100)
      descripcion = models.CharField(max_length=1000)
      precio = models.FloatField(validators=[MinValueValidator(limit_value=1)])
      stock = models.IntegerField(null=True, validators=[MinValueValidator(limit_value=0)])
      idVendedor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
      tipo = models.CharField(max_length=100)
      imagen = models.ImageField(upload_to='media/files/productos')
      