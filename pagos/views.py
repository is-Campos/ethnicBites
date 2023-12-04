from carrito.models import Carrito, CarritoDetalle
from pagos.models import Pago, MetodoDePago
from pedidos.models import Pedido, ProductoPedido
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

@csrf_exempt
def pagar(request):
    try:
        _monto = request.POST['amount'] 
        _metodoId = request.POST['metodo']
        metodoPago = MetodoDePago.objects.get(id=_metodoId)
        nuevoPedido = Pedido.objects.create(idCliente=request.user,fecha=datetime.datetime.now(),idDireccion=request.user.idDireccion)
        nuevoPedido.save()
        try:
            carrito = Carrito.objects.get(idCliente=request.user)
        except Carrito.DoesNotExist:
            return HttpResponse("No hay un carrito para este usuario")

        cart_products = CarritoDetalle.objects.filter(idCarrito=carrito)
        for cart_product in cart_products:
            producto_pedido = ProductoPedido.objects.create(idPedido=nuevoPedido, idProducto=cart_product.idProducto, cantidad=cart_product.cantidad)
            producto_pedido.save()
            product = cart_product.idProducto
            try:
                product.stock-=cart_product.cantidad
            except:
                pass
            product.save()
        
        nuevoPago = Pago.objects.create(idCliente=request.user,monto=_monto,idMetodoDePago=metodoPago,idPedido=nuevoPedido,fecha=datetime.datetime.now())
        nuevoPago.save()
    except:
        return HttpResponse("Error en el pago", status=500)
    return HttpResponse(status=200)