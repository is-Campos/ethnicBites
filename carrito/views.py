from django.http import Http404, HttpResponse
from django.shortcuts import render
from carrito.models import Carrito, CarritoDetalle
from productos.models import Producto
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def delete_from_cart(request):
    pk = request.POST['product']
    producto = Producto.objects.get(id=pk)
    try:
        carrito = Carrito.objects.get(idCliente=request.user)
    except Carrito.DoesNotExist:
       return HttpResponse("No hay un carrito para este usuario")
    try:
        cart_product = CarritoDetalle.objects.filter(idCarrito=carrito, idProducto=producto).first()
        cart_product.delete()
    except:
        return HttpResponse("Error")

    return HttpResponse(status=200)

@csrf_exempt
def delete_cart(request):
    try:
        carrito = Carrito.objects.get(idCliente=request.user)
    except Carrito.DoesNotExist:
       return HttpResponse("No hay un carrito para este usuario")
    try:
        cart_products = CarritoDetalle.objects.filter(idCarrito=carrito)
        for product in cart_products:
            product.delete()
    except:
        return HttpResponse("Error")

    return HttpResponse(status=200)

@csrf_exempt
def update_quantity_cart(request):
    pk = request.POST['product']
    new_quantity = request.POST['quantity']
    producto = Producto.objects.get(id=pk)
    try:
        carrito = Carrito.objects.get(idCliente=request.user)
    except Carrito.DoesNotExist:
       return HttpResponse("No hay un carrito para este usuario")
    try:
        cart_product = CarritoDetalle.objects.filter(idCarrito=carrito, idProducto=producto).first()
        cart_product.cantidad = new_quantity
        cart_product.save()
    except:
        return HttpResponse("Error")

    return HttpResponse(status=200)
