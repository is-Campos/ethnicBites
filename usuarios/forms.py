from django import forms
from django.forms import ModelForm
from .models import Direccion

class CrearDireccionForm(ModelForm):
    nombreCompleto = forms.TextInput
    estado = forms.TextInput
    ciudad = forms.TextInput
    codigoPostal = forms.TextInput
    colonia = forms.TextInput
    calle = forms.TextInput
    numeroExterior = forms.TextInput
    numeroInterior = forms.TextInput
    telefono = forms.TextInput

    class Meta:
        model = Direccion
        fields = ['nombreCompleto', 'estado', 'ciudad', 'codigoPostal', 'colonia', 'calle', 'numeroExterior', 'numeroInterior', 'telefono']
        labels = {
            'nombreCompleto': 'Nombre Completo',
            'codigoPostal': 'Código Postal',
            'numeroExterior': 'Número Exterior',
            'numeroInterior': 'Número Interior',
            'telefono': 'Teléfono',
        }   