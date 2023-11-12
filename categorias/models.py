from django.db import models
from productos.models import Producto

# Create your models here.

class Categoria(models.Model):
      nombre = models.CharField(max_length=100)

class CategoriaDetalle(models.Model):
      idCategoria = models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)
      idProducto = models.ForeignKey(Producto, null=True, on_delete=models.SET_NULL)
      
