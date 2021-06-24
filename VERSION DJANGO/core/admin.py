from django.contrib import admin
from .models import Categoria, Contacto,Registrar,Publicar

# Register your models here.

admin.site.register(Contacto)
admin.site.register(Registrar)
admin.site.register(Publicar)
admin.site.register(Categoria)
