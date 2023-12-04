from django.test import TestCase
from carrito.models import CarritoDetalle
from carrito.models import Carrito
from pedidos.models import Pedido
from productos.models import Producto
from pagos.models import MetodoDePago
from pagos.models import Pago
from django.contrib.auth import get_user_model
from django.urls import reverse

class Payments(TestCase):
    def test_pay(self):
        self.vendedor = get_user_model().objects.create_user(
                username='vendedor_test',
                password='password123',
                role='vendedor'
            )
        self.client.login(username='vendedor_test', password='password123')

        imagen = open("productos/files/imagenesProductos/sushi.png",'rb') 
        self.client.post(reverse('productos:crear'), {
            'nombre': 'Producto de Prueba',
            'descripcion': 'Descripción de prueba',
            'precio': 10,
            'stock': 5,
            'idVendedor':self.vendedor,
            'tipo': 'alimento',
            'imagen': imagen
        })

        producto_creado = Producto.objects.filter(nombre='Producto de Prueba').first()
        imagen = open("productos/files/imagenesProductos/sushi.png",'rb') 
        self.client.post(reverse('productos:crear'), {
            'nombre': 'Producto de Prueba2',
            'descripcion': 'Descripción de prueba2',
            'precio': 20,
            'stock': 52,
            'idVendedor':self.vendedor,
            'tipo': 'kit',
            'imagen': imagen
        })

        producto_creado2 = Producto.objects.filter(nombre='Producto de Prueba2').first()
    
        self.user = get_user_model().objects.create_user(
            username='usuario_test',
            password='password123',
            role='cliente'
        )

        self.client.login(username='usuario_test', password='password123')
        response = self.client.post(reverse('productos:add_cart'), {
            'product': producto_creado.id,
            'quantity': '2',
        })

        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('productos:add_cart'), {
            'product': producto_creado2.id,
            'quantity': '3',
        })

        self.assertEqual(response.status_code, 200)

        usuario = get_user_model().objects.get(username = 'usuario_test')

        nuevo_metodo_prueba = MetodoDePago.objects.create(nombre="Efectivo")

        response = self.client.post(reverse('pagos:pagar'), {
            'amount': 100,
            'metodo': nuevo_metodo_prueba.id,
        })

        self.assertEqual(response.status_code, 200)
        nuevoPago = Pago.objects.filter(idCliente = usuario).first()
        self.assertEqual(nuevoPago.monto,100)

    def test_error_pay(self):
        self.vendedor = get_user_model().objects.create_user(
                username='vendedor_test',
                password='password123',
                role='vendedor'
            )
        self.client.login(username='vendedor_test', password='password123')

        imagen = open("productos/files/imagenesProductos/sushi.png",'rb') 
        self.client.post(reverse('productos:crear'), {
            'nombre': 'Producto de Prueba',
            'descripcion': 'Descripción de prueba',
            'precio': 10,
            'stock': 5,
            'idVendedor':self.vendedor,
            'tipo': 'alimento',
            'imagen': imagen
        })

        producto_creado = Producto.objects.filter(nombre='Producto de Prueba').first()
        imagen = open("productos/files/imagenesProductos/sushi.png",'rb') 
        self.client.post(reverse('productos:crear'), {
            'nombre': 'Producto de Prueba2',
            'descripcion': 'Descripción de prueba2',
            'precio': 20,
            'stock': 52,
            'idVendedor':self.vendedor,
            'tipo': 'kit',
            'imagen': imagen
        })

        producto_creado2 = Producto.objects.filter(nombre='Producto de Prueba2').first()
    
        self.user = get_user_model().objects.create_user(
            username='usuario_test',
            password='password123',
            role='cliente'
        )

        self.client.login(username='usuario_test', password='password123')
        response = self.client.post(reverse('productos:add_cart'), {
            'product': producto_creado.id,
            'quantity': '2',
        })

        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('productos:add_cart'), {
            'product': producto_creado2.id,
            'quantity': '3',
        })

        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('pagos:pagar'), {
            'amount': 100,
            'metodo': '',
        })

        self.assertNotEqual(response.status_code, 200)
     