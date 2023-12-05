import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model

from usuarios.models import Direccion
from .models import Pedido, Producto, ProductoPedido

class Pedidos(TestCase):

    def test_listado_pedidos_cliente(self): 
                # Crear un cliente
        User = get_user_model()
        self.cliente = User.objects.create_user(username='cliente', password='pass')

        direccion =  Direccion.objects.create(nombreCompleto = "Casa", estado="Gto",
            ciudad = "Leon",
            codigoPostal= 58000,
            colonia= "Col",
            calle= "Calle",
            numeroExterior=1,
            numeroInterior= 1,
            telefono=1234)
        # Crear productos
        producto1 = Producto.objects.create(nombre='Producto 1', descripcion='Descripción 1', precio=100, stock=10, tipo='Tipo 1')
        producto2 = Producto.objects.create(nombre='Producto 2', descripcion='Descripción 2', precio=200, stock=20, tipo='Tipo 2')

        # Crear pedidos para el cliente
        pedido1 = Pedido.objects.create(idCliente=self.cliente, fecha=datetime.datetime.now(), idDireccion = direccion)
        ProductoPedido.objects.create(idPedido=pedido1, idProducto=producto1, cantidad=1)

        # Obtener los pedidos del cliente
        pedido_cliente = Pedido.objects.filter(idCliente=self.cliente).first()
        producto_pedido1 = ProductoPedido.objects.filter(idPedido=pedido_cliente, idProducto=producto1).first()
        producto_pedido2 = ProductoPedido.objects.filter(idPedido=pedido_cliente, idProducto=producto2).first()

        # Verificar que se obtienen los pedidos correctos    
        self.assertIsNone(producto_pedido2)
        self.assertIsNotNone(producto_pedido1)

       
    def test_visualizacion_nuevo_pedido_vendedor(self):
         # Crear un vendedor
        User = get_user_model()
        self.vendedor = User.objects.create_user(username='vendedor', password='pass')

        direccion =  Direccion.objects.create(nombreCompleto = "Casa", estado="Gto",
            ciudad = "Leon",
            codigoPostal= 58000,
            colonia= "Col",
            calle= "Calle",
            numeroExterior=1,
            numeroInterior= 1,
            telefono=1234)
        # Crear productos
        producto1 = Producto.objects.create(nombre='Producto 1', descripcion='Descripción 1', precio=100, stock=10, tipo='Tipo 1', idVendedor=self.vendedor)

        # Crear pedidos para el cliente
        self.usuario = User.objects.create_user(username='user', password='pass')
        pedido1 = Pedido.objects.create(idCliente=self.usuario, fecha=datetime.datetime.now(), idDireccion = direccion)

        ProductoPedido.objects.create(idPedido=pedido1, idProducto=producto1, cantidad=1)


        prods_vendedor = ProductoPedido.objects.filter(idPedido=pedido1)
        prods_vendedor2 = prods_vendedor.first()

        if prods_vendedor2 is not None:
            self.assertEqual(prods_vendedor2.idProducto.idVendedor, self.vendedor)
        else:
            Exception()