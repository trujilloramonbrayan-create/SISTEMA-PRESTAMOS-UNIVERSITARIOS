from rest_framework import serializers
from .models import Prestamo, Pago
from django.contrib.auth.models import User

class PrestamoSerializer(serializers.ModelSerializer):
    # Campos para lectura
    estudiante_nombre = serializers.SerializerMethodField(read_only=True)
    total_pagar = serializers.SerializerMethodField(read_only=True)
    cuota_mensual = serializers.SerializerMethodField(read_only=True)
    
    # Campo para escritura
    estudiante_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Prestamo
        fields = [
            'id', 'estudiante_id', 'estudiante_nombre',
            'monto_solicitado', 'monto_aprobado', 'tasa_interes', 
            'plazo_meses', 'fecha_solicitud', 'fecha_aprobacion',
            'fecha_desembolso', 'fecha_vencimiento', 'estado',
            'motivo', 'observaciones', 'aprobado_por',
            'total_pagar', 'cuota_mensual'
        ]
        read_only_fields = ['fecha_solicitud', 'id']
    
    def get_estudiante_nombre(self, obj):
        return f"{obj.estudiante.first_name} {obj.estudiante.last_name}"
    
    def get_total_pagar(self, obj):
        return float(obj.calcular_total_pagar())
    
    def get_cuota_mensual(self, obj):
        return float(obj.calcular_cuota_mensual())
    
    def create(self, validated_data):
        # Extraer estudiante_id
        estudiante_id = validated_data.pop('estudiante_id')
        
        # Buscar el usuario
        try:
            estudiante = User.objects.get(id=estudiante_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                'estudiante_id': f'Usuario con ID {estudiante_id} no existe'
            })
        
        # Crear el préstamo con el estudiante
        prestamo = Prestamo.objects.create(
            estudiante=estudiante,
            **validated_data
        )
        
        return prestamo
    
    def to_representation(self, instance):
        """Personalizar la respuesta para incluir datos del estudiante"""
        representation = super().to_representation(instance)
        
        # Agregar info del estudiante
        if instance.estudiante:
            representation['estudiante'] = {
                'id': instance.estudiante.id,
                'username': instance.estudiante.username,
                'first_name': instance.estudiante.first_name,
                'last_name': instance.estudiante.last_name,
                'email': instance.estudiante.email
            }
        
        return representation

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'