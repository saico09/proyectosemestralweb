from rest_framework import fields, serializers
from core.models import Registrar

class RegistrarSerializer(serializers.ModelSerializer):
    class Meta:
        model= Registrar
        fields = ['email','nombre','contrasena']