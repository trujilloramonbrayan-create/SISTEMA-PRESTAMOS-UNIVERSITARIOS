from django.db import models
from django.contrib.auth.models import User
from prestamos.models import Prestamo

class Notificacion(models.Model):
    TIPOS = [
        ('aprobacion', 'Aprobación de Préstamo'),
        ('rechazo', 'Rechazo de Préstamo'),
        ('vencimiento', 'Próximo Vencimiento'),
        ('pago', 'Recordatorio de Pago'),
        ('general', 'Notificación General'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificaciones')
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    leida = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_lectura = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"
    
    class Meta:
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"
        ordering = ['-fecha_creacion']