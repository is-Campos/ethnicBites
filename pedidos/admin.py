from django.contrib import admin

# Register your models here.

from .models import Pedido, ProductoPedido

admin.site.register(Pedido)
admin.site.register(ProductoPedido)
