from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from usuarios.forms import CrearDireccionForm
from .models import CustomUser, Direccion
from .models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from productos.models import Producto
from categorias.models import CategoriaDetalle, Categoria
from .decorators.admin_required import adminrole_required
from .decorators.vendedor_required import vendedorrole_required
from .decorators.cliente_required import clienterole_required
from django.contrib.auth.decorators import login_required


# Create your views here.


def registro(request):
    if request.method == 'GET':
        if request.user is not None:
            if request.user.role=="admin":
                return redirect('usuarios:adminHome')
            elif request.user.role=="vendedor":
                return redirect('usuarios:vendedorHome')
            elif request.user.role=="cliente":
                return redirect('productos:index')
        else:
            return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                nuevoUsuario = CustomUser.objects.create(
                    username=request.POST['username'],
                    password=make_password(request.POST['password1']),
                    role="cliente"
                    )
                nuevoUsuario.save()
                login(request, nuevoUsuario)
                return redirect('/productos')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

@login_required
def cerrarsesion(request):
    logout(request)
    return redirect('/productos')

@login_required()            
@adminrole_required()
def adminHome(request):
    if request.method == "GET":
        return render(request, 'adminHome.html')
    else:
        password2 = request.POST.get('password2')
        if request.POST.get('password') == password2:
            try:
                nuevoVendedor = CustomUser.objects.create(
                    first_name= request.POST.get('name'),
                    username= request.POST.get('username'),
                    email=request.POST.get('email'),
                    role="vendedor",
                    password=make_password(request.POST.get('password')),
                    )
                nuevoVendedor.save()
                return render(request, 'adminHome.html', {
                    'error': 'El vendedor fue creado de forma exitosa'
                })
            except IntegrityError:
                return render(request, 'adminHome.html', {
                    'error': 'El usuario ya existe'
                })
        return render(request, 'adminHome.html', {
            'error': 'Las contraseñas no coinciden'
        })

@login_required()    
@vendedorrole_required()
def vendedorHome(request):
    if request.method=="GET":
        lista_alimentos = Producto.objects.filter(idVendedor=request.user.id, tipo="alimento")
        lista_kits = Producto.objects.filter(idVendedor=request.user.id, tipo="kit")
        lista_ingredientes = Producto.objects.filter(idVendedor=request.user.id, tipo="ingrediente")
        return render(request, 'vendedorHome.html', {'listaAlimentos': lista_alimentos, 'listaKits':lista_kits, 'listaIngredientes':lista_ingredientes})

@login_required()
@vendedorrole_required()    
def modificarProducto(request,pk):
    if request.method == "GET":
        producto = Producto.objects.get(pk=pk)
        if producto is not None:
            categorias = Categoria.objects.all()
            categorias_seleccionadas = CategoriaDetalle.objects.filter(idProducto=producto.id).values_list('idCategoria', flat=True)
            return render(request, 'modificarProducto.html', {'producto':producto, 'categorias':categorias, 'categoriasSeleccionadas':categorias_seleccionadas})
        else:
            return render(request, 'modificarProducto.html', {'producto':None, 'error':"No se encontró el producto que buscabas"})
    else:
        producto = Producto.objects.get(pk=pk)
        if producto is not None:
            nombreProducto= request.POST.get('nombreproducto')
            descripcion=request.POST.get('descripcion')
            precio=request.POST.get('precio')
            stock=request.POST.get('stock')
            tipo=request.POST.get('tipo')
            imagen=request.FILES.get('imagen')
            producto.nombre=nombreProducto
            producto.descripcion=descripcion
            producto.precio=precio
            if not stock:
                producto.stock=None
            else:
                producto.stock=stock
            producto.tipo=tipo
            if imagen:
                producto.imagen = imagen
            producto.save()

            categorias_actuales = CategoriaDetalle.objects.filter(idProducto=producto.id).values_list('idCategoria', flat=True)
            categoriasSeleccionadasForm = request.POST.getlist('categorias')
            categorias_a_agregar = [int(categoria_id) for categoria_id in categoriasSeleccionadasForm if int(categoria_id) not in categorias_actuales]
            categorias_a_eliminar = [cat_id for cat_id in categorias_actuales if str(cat_id) not in categoriasSeleccionadasForm]


            for cat_id in categorias_a_agregar:
                categoria_instance = Categoria.objects.get(pk=cat_id)
                CategoriaDetalle.objects.create(idProducto=producto, idCategoria=categoria_instance)

            if categorias_a_eliminar:
                CategoriaDetalle.objects.filter(idProducto=producto.id, idCategoria__in=categorias_a_eliminar).delete()

            return redirect('usuarios:vendedorHome')
        else:
            return render(request, 'modificarProducto.html', {'producto':None, 'error':"No se pudo completar la solicitud"})

@login_required
@vendedorrole_required()
def deleteProduct(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('usuarios:vendedorHome')


@login_required()
def cerrarsesion(request):
    logout(request)
    return redirect('/productos')


def iniciarsesion(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            if request.user.role=="admin":
                return redirect('usuarios:adminHome')
            elif request.user.role=="vendedor":
                return redirect('usuarios:vendedorHome')
            elif request.user.role=="cliente":
                return redirect('productos:index')
        else:
            return render(request, 'iniciarsesion.html', {
            'form': AuthenticationForm
        })
    else:
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'iniciarsesion.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o contraseña es incorrecto'
            })
        else:
            if check_password(request.POST['password'], usuario.password):
                login(request, usuario)
                if(request.user.role=="cliente"):
                    return redirect('/productos')
                elif(request.user.role=="vendedor"):
                    return redirect('/usuarios/vendedor')
                else:
                    return redirect('/usuarios/admin')
            else:
                return render(request, 'iniciarsesion.html', {
                    'form': AuthenticationForm,
                    'error': 'El usuario o contraseña es incorrecto'
                })

@login_required()
@clienterole_required()
def direccion(request):
    direccion_usuario = None 

    if request.user.is_authenticated:
        usuarioLog = CustomUser.objects.filter(id=request.user.id).first()
        if usuarioLog and usuarioLog.idDireccion:
            direccion_usuario = usuarioLog.idDireccion
    
    if request.method == 'GET':
        form = CrearDireccionForm(instance=direccion_usuario)
        return render(request, 'direccion.html', {
            'form': form,
            'direccion_usuario': direccion_usuario,
        })

    if request.POST:
        form = CrearDireccionForm(request.POST)
        if form.is_valid():
            
            nuevaDireccion = Direccion.objects.create(nombreCompleto=request.POST['nombreCompleto'], estado=request.POST['estado'], ciudad=request.POST[
                                                    'ciudad'], codigoPostal=request.POST['codigoPostal'], colonia=request.POST['colonia'],
                                                    calle=request.POST['calle'], numeroExterior=request.POST['numeroExterior'], numeroInterior=request.POST['numeroInterior'],
                                                    telefono=request.POST['telefono'],)
            nuevaDireccion.save()
            usuario = CustomUser.objects.filter(id=request.user.id)
            if usuario:
                usuario[0].idDireccion=nuevaDireccion
                usuario[0].save()
            return redirect("/usuarios/direccion")
        else:
            return render(request, 'direccion.html', {'form': form, 'error': 'Verifica que todos los campos sean correctos'})


