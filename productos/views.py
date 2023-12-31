from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from .forms import CrearProductoForm
from .models import Producto

from categorias.models import Categoria,CategoriaDetalle
from carrito.models import CarritoDetalle
from carrito.models import Carrito
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from usuarios.decorators.vendedor_required import vendedorrole_required
from usuarios.decorators.cliente_required import clienterole_required
from usuarios.decorators.clienteornone_required import clienteornone_required
from django.contrib.auth.decorators import login_required

@clienteornone_required()
def alimentos(request): 
    all_products = Producto.objects.order_by("stock")
    return render(request,"productos/index.html",{
        'all_products': all_products
    })

@login_required()
@clienterole_required()
@csrf_exempt
def add_cart(request):
    pk = request.POST['product']
    quantity = request.POST['quantity']
    producto = Producto.objects.get(id=pk)
    try:
        carrito = Carrito.objects.get(idCliente=request.user)
    except Carrito.DoesNotExist:
        nuevoCarrito = Carrito.objects.create(idCliente=request.user)
        nuevoCarrito.save()
        carrito = nuevoCarrito
    try:
        cart_product = CarritoDetalle.objects.filter(idCarrito=carrito, idProducto=producto).first()
        cart_product.cantidad+=1
    except:
        cart_product = CarritoDetalle.objects.create(idCarrito=carrito, idProducto=producto, cantidad=quantity)    
    cart_product.save()
    return HttpResponse(status=200)

@login_required()
@vendedorrole_required()
def crear(request):
    if request.POST:
        form = CrearProductoForm(request.POST, request.FILES)
        if form.is_valid():
            stock = request.POST['stock']
            if not stock:
                stock = None
            else:
                stock = stock
            nuevoproducto = Producto.objects.create(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'], precio=request.POST[
                                                    'precio'], stock=stock, idVendedor=request.user, tipo=request.POST['tipo'], imagen=request.FILES['imagen'])
            nuevoproducto.save()
            categoriasSeleccionadasForm = request.POST.getlist('categorias')
            categorias_a_agregar = [int(categoria_id) for categoria_id in categoriasSeleccionadasForm]

            for cat_id in categorias_a_agregar:
                categoria_instance = Categoria.objects.get(pk=cat_id)
                CategoriaDetalle.objects.create(idProducto=nuevoproducto, idCategoria=categoria_instance)

            return redirect('usuarios:vendedorHome')
        else:
            return render(request, 'productos/crearproductoform.html', {'form': form, 'error': 'Verifica que todos los campos sean correctos'})

    else:
        form = CrearProductoForm(request.POST, request.FILES)
        categorias = Categoria.objects.all()
        return render(request, 'productos/crearproductoform.html', {'form': form, 'categorias':categorias})

@clienteornone_required()
def productodetalle(request, id):
    producto = Producto.objects.get(pk=id)
    if producto is not None:
        return render(request, 'productos/productodetalle.html', {'producto':producto})
    else:
        raise Http404('No pudimos encontrar la página que buscas')