from django.contrib import admin

# Register your models here.

from .models import MetodoDePago, Pago

admin.site.register(MetodoDePago)
admin.site.register(Pago)
