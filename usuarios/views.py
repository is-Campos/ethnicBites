from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

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
                    password=make_password(request.POST['password1']))
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
            # Use check_password to verify the password
            if check_password(request.POST['password'], usuario.password):
                login(request, usuario)
                return redirect('/productos')
            else:
                return render(request, 'iniciarsesion.html', {
                    'form': AuthenticationForm,
                    'error': 'El usuario o contraseña es incorrecto'
                })
