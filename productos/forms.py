from django import forms
from django.forms import ModelForm
from .models import Producto

class CrearProductoForm(ModelForm):
  nombre = forms.TextInput
  descripcion = forms.CharField(widget=forms.Textarea())
  precio = forms.NumberInput
  stock = forms.IntegerField(widget=forms.NumberInput(), required=False)
  tipo = forms.ChoiceField(choices=[('alimento', 'Alimento'), ('kit', 'Kit'), ('ingrediente', 'Ingrediente')])
  imagen = forms.ImageField
  class Meta:
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'stock', 'tipo', 'imagen']   