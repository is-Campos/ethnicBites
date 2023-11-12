from django.db import models
from usuarios.models import CustomUser
from pedidos.models import Pedido
from django.core.validators import MinValueValidator

# Create your models here.
    
class MetodoDePago(models.Model):
    nombre= models.CharField(max_length=100)

class Pago(models.Model):
    idCliente = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    monto = models.FloatField(validators=[MinValueValidator(limit_value=1)])
    idMetodoDePago = models.ForeignKey(MetodoDePago, on_delete=models.SET_NULL, null=True)
    idPedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField("fecha pago")