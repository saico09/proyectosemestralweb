from core.models import Publicar
from core.forms import ContactoForm,RegistrarForm,PublicarForm
from django.shortcuts import render,redirect


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




def eliminar(request,id):
    publicaciones=Publicar.objects.get(id=id)

    publicaciones.delete()

    return redirect(to="perfil") 