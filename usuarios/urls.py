from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "usuarios"

urlpatterns = [
  path("registro/", views.registro, name="registro"),
  path('logout/', views.cerrarsesion, name='cerrarsesion'),
  path('iniciarsesion/', views.iniciarsesion, name='iniciarsesion'),
  path('direccion/', views.direccion , name='direccion'),
  path('admin/', views.adminHome, name="adminHome"),
  path('', views.vendedorHome, name="vendedorHome"),
  path('vendedor/modificarproducto/<int:pk>', views.modificarProducto, name="modificarproducto"),
  path('vendedor/<int:pk>/delete/', views.deleteProduct, name='deleteProduct')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)