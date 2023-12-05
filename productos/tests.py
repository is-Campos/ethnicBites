from django.test import TestCase
from productos.models import Producto
from django.contrib.auth import get_user_model
from django.urls import reverse
from PIL import Image
from io import BytesIO

class Products(TestCase):
    def is_image_corrupted(self, image_data):
        try:
            Image.open(BytesIO(image_data))
            return False
        except:
            return True

    def test_create_product(self):
        
        self.vendedor = get_user_model().objects.create_user(
            username='vendedor_test',
            password='password123',
            role='vendedor'
        )
        self.client.login(username='vendedor_test', password='password123')
        imagen = open("media/files/productos/sushi.png",'rb') 
        response = self.client.post(reverse('productos:crear'), {
            'nombre': 'Producto de Prueba',
            'descripcion': 'Descripción de prueba',
            'precio': 10,
            'stock': 5,
            'idVendedor':self.vendedor,
            'tipo': 'alimento',
            'imagen': imagen
        })

        self.assertEqual(response.status_code, 302)

        producto_creado = Producto.objects.filter(nombre='Producto de Prueba').first()
        self.assertIsNotNone(producto_creado)
        self.assertEqual('Producto de Prueba', producto_creado.nombre)
        self.assertEqual('Descripción de prueba', producto_creado.descripcion)
        self.assertEqual(10, producto_creado.precio)
        self.assertEqual(5, producto_creado.stock)
        self.assertEqual(self.vendedor, producto_creado.idVendedor)
        self.assertEqual('alimento', producto_creado.tipo)
        self.assertFalse(self.is_image_corrupted(producto_creado.imagen.read()))

    def test_modify_product(self):
        self.vendedor = get_user_model().objects.create_user(
            username='vendedor_test',
            password='password123',
            role='vendedor'
        )
        self.client.login(username='vendedor_test', password='password123')
        imagen = open("media/files/productos/sushi.png",'rb') 
        response = self.client.post(reverse('productos:crear'), {
            'nombre': 'Producto de Prueba',
            'descripcion': 'Descripción de prueba',
            'precio': 10,
            'stock': 5,
            'idVendedor':self.vendedor,
            'tipo': 'alimento',
            'imagen': imagen
        })

        self.assertEqual(response.status_code, 302)

        nuevo_precio = 30
        producto_creado = Producto.objects.filter(nombre='Producto de Prueba').first()
        producto_creado.precio = nuevo_precio
        producto_creado.save()

        self.assertIsNotNone(producto_creado)     
        self.assertEqual(nuevo_precio, producto_creado.precio)
