from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import PerfilEstudiante
from .serializers import UserSerializer, PerfilEstudianteSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PerfilEstudianteViewSet(viewsets.ModelViewSet):
    queryset = PerfilEstudiante.objects.all()
    serializer_class = PerfilEstudianteSerializer