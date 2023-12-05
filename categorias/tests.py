from django.test import TestCase
from .models import Producto, Categoria, CategoriaDetalle
from django.contrib.auth import get_user_model

class Categories(TestCase):

    def setUp(self):
        # Crear categorías para la prueba
        self.cat1 = Categoria.objects.create(nombre='Kit')
        self.cat2 = Categoria.objects.create(nombre='Ingrediente')

        # Crear un usuario (vendedor)
        User = get_user_model()
        try:
            self.user = User.objects.get(username='vendedor')
        except:
            self.user = User.objects.create_user(username='vendedor', password='pass')

    def test_creacion_producto_y_filtrado_categoria(self):
        # Crear producto
        producto = Producto.objects.create(
            nombre='Tacos',
            descripcion='Kit tacos',
            precio=1000.00,
            stock=10,
            idVendedor=self.user,
            tipo='Kit'
        )

        # Asociar producto a categorías
        CategoriaDetalle.objects.create(idCategoria=self.cat1, idProducto=producto)
        CategoriaDetalle.objects.create(idCategoria=self.cat2, idProducto=producto)

        # Filtrar productos por categoría
        productos_en_kit = Producto.objects.filter(
            categoriadetalle__idCategoria=self.cat1
        )

        # Verificar que el producto está en la categoría correcta
        self.assertIn(producto, productos_en_kit)

    def test_modificacion_producto_y_filtrado_categoria(self):
                # Crear categorías para la prueba
        self.cat1 = Categoria.objects.create(nombre='Kit')
        self.cat2 = Categoria.objects.create(nombre='Ingrediente')

        # Crear un usuario (vendedor)
        User = get_user_model()
        try:
            self.user = User.objects.get(username='vendedor')
        except:
            self.user = User.objects.create_user(username='vendedor', password='pass')

           

    def test_creacion_producto_y_filtrado_categoria(self):
        # Crear producto
        producto = Producto.objects.create(
            nombre='Tamal',
            descripcion='Kit Tamal',
            precio=100.00,
            stock=10,
            idVendedor=self.user,
            tipo='Kit'
        )
        # Crear producto y asociarlo a categorías (como en el test anterior)
        # Asociar producto a categorías
        CategoriaDetalle.objects.create(idCategoria=self.cat1, idProducto=producto)
        CategoriaDetalle.objects.create(idCategoria=self.cat2, idProducto=producto)

        # Modificar producto quitando una categoría
        CategoriaDetalle.objects.filter(idCategoria=self.cat2, idProducto=producto).delete()

        # Filtrar productos por la categoría eliminada
        alimentos = Producto.objects.filter(
            categoriadetalle__idCategoria=self.cat2
        )

        # Verificar que el producto ya no está en la categoría eliminada
        self.assertNotIn(producto, alimentos)