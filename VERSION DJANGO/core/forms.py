from .models import Categoria, Contacto,Registrar,Publicar
from django.forms import ModelForm, fields
from django import forms


class ContactoForm(ModelForm):

    class Meta:
        model = Contacto
        fields = ['nombre','email','mensaje']

class RegistrarForm(ModelForm):

    class Meta:
        model = Registrar
        fields = ['email','nombre','contrasena']

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields={'descrip'}

class PublicarForm(ModelForm):

    class Meta:
        model = Publicar
        fields = ['titulo','foto','lead','noticia','categoria']