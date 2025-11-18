import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prestamos_backend.settings')
django.setup()

from django.contrib.auth.models import User
from usuarios.models import PerfilEstudiante
from prestamos.models import Prestamo, Pago
from notificaciones.models import Notificacion
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal

print("🔧 Creando datos de prueba...")

# Limpiar datos anteriores
User.objects.filter(username__in=['maria.rodriguez', 'juan.gomez', 'laura.silva']).delete()

# Obtener admin
try:
    admin = User.objects.get(username='superadmin')
    print(f"✓ Admin encontrado: {admin.username}")
except:
    print("⚠️ Creando superadmin...")
    admin = User.objects.create_superuser('superadmin', 'admin@universidad.edu.co', 'superadmin12345')
    admin.first_name = 'Administrador'
    admin.last_name = 'Sistema'
    admin.save()

# Crear perfil para admin si no existe
PerfilEstudiante.objects.get_or_create(
    usuario=admin,
    defaults={
        'rol': 'administrador',
        'codigo_estudiantil': 'ADM-001',
        'programa_academico': 'Administración',
        'semestre': 0,
        'telefono': '3201234567'
    }
)

# Estudiantes
maria = User.objects.create_user('maria.rodriguez', 'maria@universidad.edu.co', 'pass123')
maria.first_name, maria.last_name = 'María Fernanda', 'Rodríguez'
maria.save()
PerfilEstudiante.objects.create(
    usuario=maria, rol='estudiante', codigo_estudiantil='EST-2021-0156',
    programa_academico='Ingeniería de Sistemas', semestre=7, telefono='3112345678'
)
print("✓ María Rodríguez creada")

juan = User.objects.create_user('juan.gomez', 'juan@universidad.edu.co', 'pass123')
juan.first_name, juan.last_name = 'Juan Carlos', 'Gómez'
juan.save()
PerfilEstudiante.objects.create(
    usuario=juan, rol='estudiante', codigo_estudiantil='EST-2022-0287',
    programa_academico='Administración', semestre=5, telefono='3209876543'
)
print("✓ Juan Gómez creado")

laura = User.objects.create_user('laura.silva', 'laura@universidad.edu.co', 'pass123')
laura.first_name, laura.last_name = 'Laura Camila', 'Silva'
laura.save()
PerfilEstudiante.objects.create(
    usuario=laura, rol='estudiante', codigo_estudiantil='EST-2020-0423',
    programa_academico='Derecho', semestre=9, telefono='3156781234'
)
print("✓ Laura Silva creada")

# Préstamos
p1 = Prestamo.objects.create(
    estudiante=maria, monto_solicitado=Decimal('5000000'),
    tasa_interes=Decimal('0'), plazo_meses=12, estado='pendiente',
    motivo='Préstamo para matrícula y computador.'
)
print("✓ Préstamo pendiente creado")

p2 = Prestamo.objects.create(
    estudiante=juan, monto_solicitado=Decimal('3500000'),
    monto_aprobado=Decimal('3500000'), tasa_interes=Decimal('4.5'),
    plazo_meses=10, estado='aprobado',
    fecha_aprobacion=timezone.now() - timedelta(days=2),
    aprobado_por=admin, motivo='Matrícula y material didáctico.'
)
print("✓ Préstamo aprobado creado")

p3 = Prestamo.objects.create(
    estudiante=laura, monto_solicitado=Decimal('4000000'),
    monto_aprobado=Decimal('4000000'), tasa_interes=Decimal('3.8'),
    plazo_meses=12, estado='activo',
    fecha_aprobacion=timezone.now() - timedelta(days=40),
    fecha_desembolso=timezone.now() - timedelta(days=35),
    fecha_vencimiento=(timezone.now() + timedelta(days=300)).date(),
    aprobado_por=admin, motivo='Especialización en Derecho.'
)
print("✓ Préstamo activo creado")

# Pagos
Pago.objects.create(prestamo=p3, monto=Decimal('346666.67'), metodo_pago='transferencia', comprobante='TRF-001', registrado_por=admin)
Pago.objects.create(prestamo=p3, monto=Decimal('346666.67'), metodo_pago='transferencia', comprobante='TRF-002', registrado_por=admin)
print("✓ 2 Pagos creados")

# Notificaciones
Notificacion.objects.create(
    usuario=maria, prestamo=p1, tipo='general',
    titulo='Solicitud recibida',
    mensaje='Tu solicitud de $5.000.000 está en revisión.'
)
Notificacion.objects.create(
    usuario=juan, prestamo=p2, tipo='aprobacion',
    titulo='¡Préstamo aprobado!',
    mensaje='Tu solicitud de $3.500.000 fue aprobada.',
    leida=True, fecha_lectura=timezone.now() - timedelta(days=1)
)
print("✓ 2 Notificaciones creadas")

print("\n✅ DATOS CREADOS:")
print(f"   Usuarios: {User.objects.count()}")
print(f"   Préstamos: {Prestamo.objects.count()}")
print(f"   Pagos: {Pago.objects.count()}")
print(f"   Notificaciones: {Notificacion.objects.count()}")
print("\n🔑 Credenciales:")
print("   superadmin / superadmin12345")
print("   maria.rodriguez / pass123")
print("   juan.gomez / pass123")
print("   laura.silva / pass123")