from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from usuarios.views import UserViewSet, PerfilEstudianteViewSet
from prestamos.views import PrestamoViewSet, PagoViewSet
from notificaciones.views import NotificacionViewSet

router = DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'perfiles', PerfilEstudianteViewSet)
router.register(r'prestamos', PrestamoViewSet)
router.register(r'pagos', PagoViewSet)
router.register(r'notificaciones', NotificacionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]