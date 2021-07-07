from django.urls import path
from .views import procesar_periodistas, detalle_periodista



urlpatterns =[
    path('periodistas/',procesar_periodistas,name="procesar_periodistas"),
    path('periodistas/<id>',detalle_periodista,name="detalle_periodista")
]