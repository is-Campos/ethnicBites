from django import forms
from django.forms import ModelForm
from .models import Producto

class CrearProductoForm(ModelForm):
<<<<<<< HEAD
  nombre = forms.TextInput
  descripcion = forms.CharField(widget=forms.Textarea())
  precio = forms.NumberInput
  stock = forms.IntegerField(widget=forms.NumberInput(), required=False)
  tipo = forms.ChoiceField(choices=[('alimento', 'Alimento'), ('kit', 'Kit'), ('ingrediente', 'Ingrediente')])
  imagen = forms.ImageField
=======
  nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
  precio = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
  stock = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
  tipo = forms.ChoiceField(choices=[('alimento', 'Alimento'), ('kit', 'Kit'), ('ingrediente', 'Ingrediente')], widget=forms.Select(attrs={'class': 'form-select'}))
  imagen = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
>>>>>>> remote/master
  class Meta:
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'stock', 'tipo', 'imagen']   