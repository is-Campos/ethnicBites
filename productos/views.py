from http.client import HTTPResponse
from django.http import Http404
from django.shortcuts import redirect, render
from django.views import generic
from .forms import CrearProductoForm
from .models import Producto
from carrito.models import CarritoDetalle
from carrito.models import Carrito
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


def alimentos(request): 
    all_products = Producto.objects.order_by("stock")
    return render(request,"productos/index.html",{
        'all_products': all_products
    })

@csrf_exempt
def add_cart(request):
    producto = Producto.objects.get(pk=1)
    try:
        carrito = Carrito.objects.get(idCliente=request.user)
        return render(request, 'productos/productodetalle.html', {'producto':producto})
    except Carrito.DoesNotExist:
        nuevoCarrito = Carrito.objects.create(idCliente=request.user)
        nuevoCarrito.save()
        return render(request, 'productos/index.html')

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
            return redirect('/productos')
        else:
            return render(request, 'productos/crearproductoform.html', {'form': form, 'error': 'Verifica que todos los campos sean correctos'})

    else:
        form = CrearProductoForm(request.POST, request.FILES)
        return render(request, 'productos/crearproductoform.html', {'form': form})

def productodetalle(request, id):
    producto = Producto.objects.get(pk=id)
    if producto is not None:
        return render(request, 'productos/productodetalle.html', {'producto':producto})
    else:
        raise Http404('No pudimos encontrar la página que buscas')