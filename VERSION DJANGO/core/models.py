from django.core.files.base import File
from django.db import models
from django.db.models.fields import EmailField
from django.forms.widgets import FileInput



#Clase Contacto



class Contacto(models.Model):

    nombre = models.CharField(max_length=20, verbose_name="Nombre ",null=True)
    email = models.EmailField(max_length=60, verbose_name="Email ",null=True)
    mensaje = models.TextField(max_length=100, verbose_name="Mensaje ",null=True)

    def __str__(self):

        return self.nombre


class Registrar(models.Model):

    email = models.EmailField(max_length=60, verbose_name="Email ",null=True)
    nombre = models.CharField(max_length=20, verbose_name="Nombre ",null=True)
    contrasena = models.CharField(max_length=20, verbose_name="Contrasena ",null=True)

    def __str__(self):

        return self.email

class Categoria(models.Model):

    descrip = models.CharField(max_length=200, verbose_name="descrip ",null=True)

    def __str__(self):

        return self.descrip

class Publicar(models.Model):

    titulo = models.CharField(max_length=200, verbose_name="Titulo ",null=True)
    foto= models.ImageField(null=True, verbose_name='image')
    lead = models.TextField(max_length=1000, verbose_name="lead ",null=True)
    noticia = models.TextField(max_length=2200, verbose_name="noticia ",null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):

        return self.categoria
