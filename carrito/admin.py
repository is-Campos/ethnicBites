from django.contrib import admin

# Register your models here.

from .models import Carrito, CarritoDetalle

admin.site.register(Carrito)
admin.site.register(CarritoDetalle)
