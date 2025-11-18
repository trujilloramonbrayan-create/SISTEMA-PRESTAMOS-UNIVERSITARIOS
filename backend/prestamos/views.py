from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Prestamo, Pago
from .serializers import PrestamoSerializer, PagoSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    
    @action(detail=False, methods=['get'])
    def pendientes(self, request):
        prestamos = self.queryset.filter(estado='pendiente')
        serializer = self.get_serializer(prestamos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def activos(self, request):
        prestamos = self.queryset.filter(estado='activo')
        serializer = self.get_serializer(prestamos, many=True)
        return Response(serializer.data)

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer