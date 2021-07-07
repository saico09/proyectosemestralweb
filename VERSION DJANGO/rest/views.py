from .serializers import RegistrarSerializer
from django.shortcuts import render
from core.models import Registrar
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view (['GET','POST','DELETE'])
@permission_classes((IsAuthenticated,))
def procesar_periodistas(request):

    if request.method == 'GET':
        periodistas = Registrar.objects.all()
        serializer=RegistrarSerializer(periodistas,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer=RegistrarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view (['GET','PUT','DELETE']) 

def detalle_periodista(request,id):
    try:
        periodistas= Registrar.objects.get(id=id)
    except Registrar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistrarSerializer(periodistas)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RegistrarSerializer(periodistas,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    if request.method == 'DELETE':
        periodistas.delete()
        return Response(status.HTTP_204_NO_CONTENT)