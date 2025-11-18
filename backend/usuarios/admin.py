from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import PerfilEstudiante

class PerfilEstudianteInline(admin.StackedInline):
    model = PerfilEstudiante
    can_delete = False
    verbose_name_plural = 'Perfil'

class UserAdmin(BaseUserAdmin):
    inlines = (PerfilEstudianteInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_rol', 'is_staff')
    
    def get_rol(self, obj):
        try:
            return obj.perfil.get_rol_display()
        except:
            return '-'
    get_rol.short_description = 'Rol'

# Re-registrar UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(PerfilEstudiante)
class PerfilEstudianteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'codigo_estudiantil', 'programa_academico', 'semestre', 'activo')
    list_filter = ('activo', 'programa_academico', 'semestre')
    search_fields = ('usuario__username', 'codigo_estudiantil', 'usuario__first_name', 'usuario__last_name')
    readonly_fields = ('fecha_registro',)