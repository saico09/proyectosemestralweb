from core.models import Publicar
from core.models import Registrar
from core.forms import ContactoForm,RegistrarForm,PublicarForm
from django.shortcuts import redirect, render


def index(request):
    datos = {

        'form1' : RegistrarForm()

    }
    if request.method == 'POST':
        formulario = RegistrarForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            datos['mensaje']= 'Datos guardados exitosamente'
    return render (request,'core/index.html',datos)

def contacto(request):
    datos = {

        'form' : ContactoForm()

    }
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            datos['mensaje']= 'Datos guardados exitosamente'

    return render(request,'core/CAOS NEWS contacto.html',datos)

def politica(request,categoria):
    publicaciones=Publicar.objects.filter(categoria=categoria)

    datos = {
        'politica': publicaciones
    }

    return render (request,'core/CAOS NEWS 1politica.html',datos)

def perfil(request):
        
    publicaciones=Publicar.objects.all()

    datos = {
        'publicaciones': publicaciones
    }
    return render (request,'core/CAOS NEWS perfil.html',datos)

def perfil2(request,id):
        
    perfil=Registrar.objects.filter(id=id)

    datos = {
        'perfil': perfil
    }

    return render (request,'core/CAOS NEWS perfil copia.html',datos)


def publicar(request):
    datos = {

        'form2' : PublicarForm()

    }
    if request.method == 'POST':
        formulario = PublicarForm(request.POST,request.FILES)

        if formulario.is_valid():
            formulario.save()
            datos['mensaje']= 'Datos guardados exitosamente'

    return render (request,'core/CAOS NEWS publicar.html',datos)



def modificar(request,id):
    publicaciones=Publicar.objects.get(id=id)

    datos = {
        'form': PublicarForm(instance=publicaciones)
    }

    if request.method== 'POST':
        formulario=PublicarForm(data=request.POST,instance=publicaciones)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Datos modificados exitosamente"

    return render(request,'core/CAOS NEWS editar pub.html',datos)

def noticia(request,id):
    publicaciones=Publicar.objects.filter(id=id)

    datos = {
        'noticia': publicaciones
    }

    return render (request,'core/CAOS NEWS NOTICIA.html',datos)


def carrucel(request):
    publicaciones=Publicar.objects.all()

    datos = {
        'publicaciones': publicaciones
    }
    return render (request,'core/index.html',datos) 

def eliminar(request,id):
    publicaciones=Publicar.objects.get(id=id)

    publicaciones.delete()

    return redirect(to="perfil")

def periodistas(request):
    periodistas=Registrar.objects.all()

    datos = {
        'periodistas': periodistas
    }
    return render (request,'core/CAOS NEWS periodistas.html',datos)

def eliminarpe(request,id):
    periodistas=Registrar.objects.get(id=id)

    periodistas.delete()

    return redirect(to="periodistas")
