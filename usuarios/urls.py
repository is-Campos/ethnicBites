from django.urls import path

from . import views

app_name = "usuarios"

urlpatterns = [
  path("registro/", views.registro, name="registro"),
  path('logout/', views.cerrarsesion, name='cerrarsesion'),
  path('iniciarsesion/', views.iniciarsesion, name='iniciarsesion'),
  path('admin/', views.adminHome, name="adminHome"),
  path('vendedor/', views.vendedorHome, name="vendedorHome"),
  path('vendedor/modificarproducto/<int:pk>', views.modificarProducto, name="modificarproducto"),
  path('vendedor/<int:pk>/delete/', views.deleteProduct, name='deleteProduct'),
]