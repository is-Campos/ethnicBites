from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "pagos"

urlpatterns = [
  path("nuevo/", views.pagar, name="pagar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)