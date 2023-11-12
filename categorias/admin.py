from django.contrib import admin

# Register your models here.

from .models import Categoria, CategoriaDetalle

admin.site.register(Categoria)
admin.site.register(CategoriaDetalle)
