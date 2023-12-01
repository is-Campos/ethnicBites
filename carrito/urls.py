from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from productos import views
from . import views

app_name = "carrito"

urlpatterns = [
    path("", views.cart, name="index")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)