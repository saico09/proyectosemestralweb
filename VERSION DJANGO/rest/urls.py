from django.urls import path
from .views import procesar_periodistas,detalle_periodista
from .viewslogin import login


urlpatterns =[
    path('periodistas/',procesar_periodistas,name="procesar_periodistas"),
    path('periodistas/<id>',detalle_periodista,name="detalle_periodista"),
    path('login',login,name="login"),
]