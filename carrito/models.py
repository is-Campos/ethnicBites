from django.db import models
from productos.models import Producto
from usuarios.models import CustomUser
from django.core.validators import MinValueValidator

# Create your models here.

class Carrito(models.Model):
      idCliente = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

class CarritoDetalle(models.Model):
      idCarrito = models.ForeignKey(Carrito, on_delete=models.CASCADE,)
      idProducto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
      cantidad = models.IntegerField(validators=[MinValueValidator(limit_value=1)], null=True)
