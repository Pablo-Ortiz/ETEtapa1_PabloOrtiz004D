from django import forms
from django.forms import ModelForm, fields
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Usuario, Pais


class UsuarioForm(forms.ModelForm):

    class Meta:
        model=Usuario
        fields = ['RutUsuario','nombreCom', 'telefono', 'direccion', 'email', 'idPais', 'image', 'passw']
        
        labels = '__all__'

        widgets={
            'RutUsuario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su rut',
                    'id': 'RutUsuario'
                }
            ),
            'nombreCom': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre completo',
                    'id': 'nombreCom'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su telefono',
                    'id': 'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su direccion',
                    'id': 'direccion'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo',
                    'id': 'email'
                }
            ),
            'idPais': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione su país',
                    'id': 'pais'
                }
            ),
            'image':forms.ClearableFileInput(
            attrs={
                'class':'form-control',
                'id': 'image'
            }
            ),
            'passw': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su contraseña',
                    'id': 'passw'
                }
            )
        }

#class UsuarioForm(forms.ModelForm)
#    RutUsuario = forms.CharField(label='Rut del usuario',max_length=10,widgets=forms.TextInput )