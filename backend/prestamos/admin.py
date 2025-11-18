from django.contrib import admin
from .models import Prestamo, Pago

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudiante', 'monto_solicitado', 'monto_aprobado', 'estado', 'fecha_solicitud', 'plazo_meses')
    list_filter = ('estado', 'fecha_solicitud')
    search_fields = ('estudiante__username', 'estudiante__first_name', 'estudiante__last_name')
    readonly_fields = ('fecha_solicitud', 'calcular_total_pagar', 'calcular_cuota_mensual')
    
    fieldsets = (
        ('Información del Estudiante', {
            'fields': ('estudiante', 'motivo')
        }),
        ('Detalles del Préstamo', {
            'fields': ('monto_solicitado', 'monto_aprobado', 'tasa_interes', 'plazo_meses')
        }),
        ('Cálculos', {
            'fields': ('calcular_total_pagar', 'calcular_cuota_mensual'),
            'classes': ('collapse',)
        }),
        ('Fechas', {
            'fields': ('fecha_solicitud', 'fecha_aprobacion', 'fecha_desembolso', 'fecha_vencimiento')
        }),
        ('Estado y Aprobación', {
            'fields': ('estado', 'aprobado_por', 'observaciones')
        }),
    )
    
    actions = ['aprobar_prestamos', 'rechazar_prestamos']
    
    def aprobar_prestamos(self, request, queryset):
        from django.utils import timezone
        queryset.update(estado='aprobado', fecha_aprobacion=timezone.now(), aprobado_por=request.user)
        self.message_user(request, f"{queryset.count()} préstamos aprobados.")
    aprobar_prestamos.short_description = "Aprobar préstamos seleccionados"
    
    def rechazar_prestamos(self, request, queryset):
        queryset.update(estado='rechazado')
        self.message_user(request, f"{queryset.count()} préstamos rechazados.")
    rechazar_prestamos.short_description = "Rechazar préstamos seleccionados"

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'prestamo', 'monto', 'fecha_pago', 'metodo_pago', 'registrado_por')
    list_filter = ('metodo_pago', 'fecha_pago')
    search_fields = ('prestamo__estudiante__username', 'comprobante')
    readonly_fields = ('fecha_pago',)