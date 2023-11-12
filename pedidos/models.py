from django.db import models
from usuarios.models import CustomUser, Direccion
from django.core.validators import MinValueValidator
from productos.models import Producto
# Create your models here.

class Pedido(models.Model):
      idCliente = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
      fecha = models.DateTimeField("fecha pedido")
      idDireccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True)

class ProductoPedido(models.Model):
      idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
      idProducto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
      cantidad = models.IntegerField(validators=[MinValueValidator(limit_value=1)])