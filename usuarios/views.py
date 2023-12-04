from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from .forms import CrearDireccionForm
from .models import Direccion
from usuarios.models import CustomUser
# Create your views here.


def registro(request):

    if request.method == 'GET':
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


def cerrarsesion(request):
    logout(request)
    return redirect('/productos')


def iniciarsesion(request):
    if request.method == 'GET':
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
                return redirect('/productos')
            else:
                return render(request, 'iniciarsesion.html', {
                    'form': AuthenticationForm,
                    'error': 'El usuario o contraseña es incorrecto'
                })

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