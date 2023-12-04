from django.http import Http404
from django.shortcuts import redirect, render
from django.views import generic
from .forms import CrearProductoForm
from .models import Producto
from categorias.models import Categoria,CategoriaDetalle


class IndexView(generic.TemplateView):
    template_name = "productos/index.html"


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

def productodetalle(request, id):
    producto = Producto.objects.get(pk=id)
    if producto is not None:
        return render(request, 'productos/productodetalle.html', {'producto':producto})
    else:
        raise Http404('No pudimos encontrar la página que buscas')