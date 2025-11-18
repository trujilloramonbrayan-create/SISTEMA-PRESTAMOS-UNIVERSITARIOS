from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PerfilEstudiante

class PerfilEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilEstudiante
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    perfil = PerfilEstudianteSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'perfil']