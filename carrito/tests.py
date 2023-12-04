from django.test import TestCase
from carrito.models import CarritoDetalle
from carrito.models import Carrito
from productos.models import Producto
from django.contrib.auth import get_user_model
from django.urls import reverse

class Cart(TestCase):

    def test_add_product_to_cart(self):
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

        usuario = get_user_model().objects.get(username = 'usuario_test')

        carrito = Carrito.objects.get(idCliente=usuario)
        cart_product = CarritoDetalle.objects.filter(idCarrito=carrito, idProducto=producto_creado).first()

        self.assertEqual(cart_product.idProducto, producto_creado)
        self.assertEqual(cart_product.cantidad, 2)

    def test_delete_from_cart(self):
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

        response = self.client.post(reverse('carrito:delete_from_cart'), {
            'product': producto_creado.id
        })

        self.assertEqual(response.status_code, 200)

        carrito = Carrito.objects.get(idCliente=usuario)
        cart_product1 = CarritoDetalle.objects.filter(idCarrito=carrito, idProducto=producto_creado).first()
        cart_product2 = CarritoDetalle.objects.filter(idCarrito=carrito, idProducto=producto_creado2).first()

        self.assertIsNone(cart_product1)  
        self.assertIsNotNone(cart_product2) 

        
