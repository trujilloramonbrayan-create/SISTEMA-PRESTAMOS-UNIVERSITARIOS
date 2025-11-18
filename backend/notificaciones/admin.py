from django.contrib import admin
from .models import Notificacion

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'tipo', 'leida', 'fecha_creacion')
    list_filter = ('tipo', 'leida', 'fecha_creacion')
    search_fields = ('titulo', 'mensaje', 'usuario__username')
    readonly_fields = ('fecha_creacion', 'fecha_lectura')
    
    actions = ['marcar_como_leida']
    
    def marcar_como_leida(self, request, queryset):
        from django.utils import timezone
        queryset.update(leida=True, fecha_lectura=timezone.now())
        self.message_user(request, f"{queryset.count()} notificaciones marcadas como leídas.")
    marcar_como_leida.short_description = "Marcar como leída"