from django.urls import path

from . import views

app_name = "usuarios"

urlpatterns = [
  path("registro/", views.registro, name="registro"),
  path('logout/', views.cerrarsesion, name='cerrarsesion'),
  path('iniciarsesion/', views.iniciarsesion, name='iniciarsesion')
]