from django.urls import path
from .views import index
from .views import contacto
from .views import politica,perfil,publicar,modificar,noticia,carrucel,eliminar,periodistas,perfil2
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('',index, name ='index'),
    path('contacto/',contacto, name ='contacto'),
    path('perfil/',perfil, name='perfil'),
    path('publicar/',publicar, name='publicar'),
    path('periodistas/',periodistas, name='periodistas'), 
    path('perfil2/<id>',perfil2, name='perfil2'),  
    path('noticiasss/<categoria>',politica, name ='politica'), 
    path('noticia/<id>',noticia, name='noticia'),

    path('modificar/<id>',modificar,name='modificar'),
    path('eliminar/<id>',eliminar,name='eliminar'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

