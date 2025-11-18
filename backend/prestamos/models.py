from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Prestamo(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('activo', 'Activo'),
        ('finalizado', 'Finalizado'),
        ('rechazado', 'Rechazado'),
        ('vencido', 'Vencido'),
    ]
    
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prestamos')
    monto_solicitado = models.DecimalField(max_digits=10, decimal_places=2)
    monto_aprobado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    plazo_meses = models.IntegerField()
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_aprobacion = models.DateTimeField(null=True, blank=True)
    fecha_desembolso = models.DateTimeField(null=True, blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    
    motivo = models.TextField()
    observaciones = models.TextField(blank=True)
    aprobado_por = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='prestamos_aprobados'
    )
    
    def calcular_total_pagar(self):
        if self.monto_aprobado and self.tasa_interes:
            interes = self.monto_aprobado * (self.tasa_interes / 100)
            return self.monto_aprobado + interes
        return 0
    
    def calcular_cuota_mensual(self):
        if self.plazo_meses > 0:
            return self.calcular_total_pagar() / self.plazo_meses
        return 0
    
    def __str__(self):
        return f"Préstamo #{self.id} - {self.estudiante.username} - ${self.monto_solicitado}"
    
    class Meta:
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos"
        ordering = ['-fecha_solicitud']


class Pago(models.Model):
    METODOS_PAGO = [
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia'),
        ('tarjeta', 'Tarjeta'),
        ('consignacion', 'Consignación'),
    ]
    
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO)
    comprobante = models.CharField(max_length=100, blank=True)
    observaciones = models.TextField(blank=True)
    registrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"Pago #{self.id} - ${self.monto} - {self.fecha_pago.date()}"
    
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ['-fecha_pago']