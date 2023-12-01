from django.shortcuts import render
from carrito.models import Carrito, CarritoDetalle
from productos.models import Producto

#def get_cart(request): 
    #return render(request,"carrito.html")

def cart(request):
    try:
        carrito = Carrito.objects.get(idCliente=request.user)
        try:
            cart_products = CarritoDetalle.objects.filter(idCarrito=carrito.id)
        except:
            #NO HAY PRODUCTOS EN CARRITO
            return 
    except Carrito.DoesNotExist:
        nuevoCarrito = Carrito.objects.create(idCliente=request.user)
        nuevoCarrito.save()
        return 
    
    return render(request,"carrito.html",{
        'cart_products': cart_products
    })
