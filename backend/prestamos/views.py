from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Prestamo, Pago
from .serializers import PrestamoSerializer, PagoSerializer
from notificaciones.models import Notificacion  # ← IMPORTANTE

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            prestamo = serializer.save()

            # 🔥 Crear notificación automática
            Notificacion.objects.create(
                usuario=prestamo.estudiante,
                mensaje=f"Tu solicitud de préstamo por ${prestamo.monto_solicitado} fue enviada correctamente."
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # DEBUG
        print("DEBUG ERROR:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
