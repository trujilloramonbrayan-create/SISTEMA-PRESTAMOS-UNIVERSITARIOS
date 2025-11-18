from django.db import models
from django.contrib.auth.models import User

class PerfilEstudiante(models.Model):
    ROLES = [
        ('estudiante', 'Estudiante'),
        ('administrador', 'Administrador'),
    ]
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(max_length=20, choices=ROLES, default='estudiante')
    codigo_estudiantil = models.CharField(max_length=20, unique=True)
    programa_academico = models.CharField(max_length=100)
    semestre = models.IntegerField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.usuario.get_full_name()} - {self.codigo_estudiantil}"
    
    class Meta:
        verbose_name = "Perfil de Estudiante"
        verbose_name_plural = "Perfiles de Estudiantes"