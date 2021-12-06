from django import forms
from .models import Mesa, Inventario, Solicitud, Receta, Reserva, Orden
from datetime import datetime 

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ("nro_mesa",)
        labels = {
            'nro_mesa': 'Mesa Asignada'
        }
        widgets = {
            'nro_mesa': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese una mesa'
                }
            )
        }


class InventarioForm(forms.ModelForm):

    class Meta:
        model = Inventario
        fields = ('producto','stock','nombre_encargado','fecha_ult_revision')
        label = {
            'producto':'Producto',
            'nombre_encargado': 'Encargado',
            'fecha_ult_revision': 'Ultima fecha de revision'
        }
        widgets = {
            'producto': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto'
                }
            ),
            'nombre_encargado': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'fecha_ult_revision': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control'
                }
            )
        }

class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = ('insumo','cantidad', 'fecha_solicitud', 'nombre_solicitante')
        label = {
            'insumo': 'Insumo',
            'cantidad': 'Cantidad',
            'fecha_solicitud': 'Fecha de Solicitud',
            'nombre_solicitante': 'Nombre de solicitante'
        }
        widgets ={
            'insumo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del insumo'
                }

            ),
            'cantidad':forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Cantidad'
                }

            ),
            'fecha_solicitud':forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control'
                }

            ),
            'nombre_solicitante':forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del solicitante'
                }

            )


        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('cliente', 'fecha_creacion','fecha_cierre', 'mesa','notas')
        label = {
            'cliente':'Nombre Cliente',
            'fecha_creacion': 'Fecha Comienzo',
            'fecha_cierre': 'Fecha Termino',
            'mesa':'Numero de la mesa',
            'notas': 'Notas'
        }
        widgets={
            'cliente': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'fecha_creacion': forms.DateTimeInput(
                attrs= {
                    'class': 'form-control'
                }
            ),
            'fecha_cierre': forms.DateTimeInput(
                attrs= {
                    'class': 'form-control'
                }
            ),
            'mesa': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'notas': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese algun comentario..'
                }
            )
        }

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('titulo', 'descripcion','ingredientes','instrucciones','precio','imagen')
        label = {
            'titulo':'Titulo',
            'descripcion': 'Descripción',
            'ingredientes':'Ingredientes',
            'instrucciones':'Instrucciones',
            'precio':'Precio $:',
            'imagen':'Imagen',

        }
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Ingrese el nombre del platillo'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una descripcion el platillo'
                }
            ),
            'ingredientes': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los ingrediente a utilizar ej: 2 cucharadas de sal - 1kg de harina- media taza de agua'
                }
            ),
            'instrucciones': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los pasos a seguir'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el valor del plato'
                }

            ),

        }
class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ('mesa','prioridad')
        label= {
            'mesa':'Nro de Mesa',
            'prioridad':'Prioridad',
        }

        widgets= {
            'mesa': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'prioridad': forms.Select(
                choices= {
                    (1,'Aperitivo'),
                    (2,'Entrada'),
                    (3,'Principal'),
                    (4,'Postre'),
                },
                attrs={
                    'class': 'form-control'
                }
            )
        }
 
        
