from rest_framework import serializers
from .models import Prestamo, Pago
from usuarios.serializers import UserSerializer

class PrestamoSerializer(serializers.ModelSerializer):
    estudiante = UserSerializer(read_only=True)
    total_pagar = serializers.SerializerMethodField()
    cuota_mensual = serializers.SerializerMethodField()
    
    class Meta:
        model = Prestamo
        fields = '__all__'
    
    def get_total_pagar(self, obj):
        return obj.calcular_total_pagar()
    
    def get_cuota_mensual(self, obj):
        return obj.calcular_cuota_mensual()

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'