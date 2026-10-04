from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Comida, Cliente, Usuario

class ComidaFrom(forms.ModelForm):
    
    class Meta:
        model = Comida
        fields = ['marca', 'nombre', 'tamanno', 'categoria']
        lables = {
            'marca' : 'Marca',
            'nombre' : 'Nombre',
            'tamanno' : 'Tamanno',
            'categoria' : 'Categoria'
            }
        widgets = {
            'marca' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese marca',
                    'id': 'marca'
                }
            ),
            'nombre' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre',
                    'id': 'nombre'
                }
            ),
            'tamanno' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese tamaño',
                    'id': 'tamanno'
                }
            ),
            'categoria' : forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )
        }


class ClienteForm(ModelForm):


    class Meta:
        model = Cliente
        fields =['rut','nombre','gmail','telefono','direccion','usuario']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'gmail': 'gmail',
            'telefono': 'telefono',
            'usuario': 'usuario'
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ),
            'gmail': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese mail', 
                    'id': 'gamil'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese telefono', 
                    'id': 'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direccion'
                }
            ),
            'usuario': forms.Select(
                attrs={
                    'class': 'form-control', 
                    'id': 'usuario'
                }
            )
        }