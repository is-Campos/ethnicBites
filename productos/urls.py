from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "productos"

urlpatterns = [
  path("", views.alimentos, name="index"),
  path('crear/', views.crear, name='crear'),
  path('<int:id>', views.productodetalle),
  path('add_cart/', views.add_cart, name='add_cart')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)