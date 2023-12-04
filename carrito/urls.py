from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from productos import views
from . import views

app_name = "carrito"

urlpatterns = [
    path("", views.cart, name="index"),
    path('delete_from_cart/', views.delete_from_cart,name='delete_from_cart'),
    path('delete_cart/', views.delete_cart),
    path('update_quantity_cart/', views.update_quantity_cart)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)