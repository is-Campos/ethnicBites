from django.contrib import admin

# Register your models here.

from .models import CustomUser, Direccion

admin.site.register(CustomUser)
admin.site.register(Direccion)