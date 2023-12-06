from django.http import Http404
from django.shortcuts import redirect, render
from .models import Pedido, ProductoPedido
from productos.models import Producto
from usuarios.decorators.corv_required import corv_required
from django.contrib.auth.decorators import login_required

class pedidoVendedor:
    def __init__(self, productos, idPedido, total):
        self.productos = productos
        self.idPedido = idPedido
        self.total = total

@login_required()
@corv_required()
def pedidos(request):

        # return render (request, "pedidos.html")
        if request.user.role=="cliente":
          lista_pedidos_cliente = Pedido.objects.filter(idCliente=request.user.id).order_by('-fecha').values_list('id', flat=True)
          lista_productospedidos_cliente = ProductoPedido.objects.filter(idPedido__in=lista_pedidos_cliente)

          listapedidos=[]

          def getPedidosCliente():
            for productopedido in lista_productospedidos_cliente:
               pedido_existente = next((pedido for pedido in listapedidos if pedido.idPedido == productopedido.idPedido), None)
               if pedido_existente:
                  pedido_existente.productos.append(productopedido)
               else:
                  NuevoPedido = pedidoVendedor([productopedido], productopedido.idPedido, total=0)
                  listapedidos.append(NuevoPedido)

            total = 0
            for pedido in listapedidos:
              for producto in pedido.productos:
                total += producto.idProducto.precio * producto.cantidad
              pedido.total = total
              total = 0
            
            return listapedidos
          
          listapedidoscliente = getPedidosCliente()    
          return render (request, "pedidos.html", {'lista_pedidos': listapedidoscliente, 'error': "Aún no tienes pedidos", 'template':"cliente"})
        else:
          lista_idsproductos_vendedor = Producto.objects.filter(idVendedor=request.user.id).values_list('id', flat=True)
          lista_productosPedidosVendedor = ProductoPedido.objects.filter(idProducto__in=lista_idsproductos_vendedor).order_by('-idPedido__fecha')

          
          def getPedidosVendedor():
            listapedidos = []
    
            for productopedido in lista_productosPedidosVendedor:
                # Intentar encontrar un pedido existente para este producto
                pedido_existente = next((pedido for pedido in listapedidos if pedido.idPedido == productopedido.idPedido), None)

                if pedido_existente:
                    # Si ya existe un pedido para este producto, agregarlo a ese pedido existente
                    pedido_existente.productos.append(productopedido)
                else:
                    # Si no existe un pedido para este producto, crear un nuevo pedido
                    NuevoPedido = pedidoVendedor([productopedido], productopedido.idPedido, total=0)
                    listapedidos.append(NuevoPedido)

            total = 0
            for pedido in listapedidos:
              for producto in pedido.productos:
                total += producto.idProducto.precio * producto.cantidad
              pedido.total = total
              total = 0

            return listapedidos

          lista_pedidosVendedor = getPedidosVendedor()
          return render (request, "pedidos.html", {'lista_pedidos_vendedor': lista_pedidosVendedor, 'error': "Aún no tienes pedidos", 'template':"vendedor"})