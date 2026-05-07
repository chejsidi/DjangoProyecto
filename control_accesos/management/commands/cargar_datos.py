from django.core.management.base import BaseCommand
from control_accesos.models import Usuario, Zona, Permiso, RegistroAcceso
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Carga datos de prueba realistas'

    def handle(self, *args, **kwargs):
        # Usuarios
        usuarios_data = [
            ('12345678A', 'Ana',    'García López',    'ana@egibide.org',    '600111001', 'empleado'),
            ('23456789B', 'Carlos', 'Martínez Ruiz',   'carlos@egibide.org', '600111002', 'empleado'),
            ('34567890C', 'Laura',  'Sánchez Pérez',   'laura@egibide.org',  '600111003', 'admin'),
            ('45678901D', 'Pedro',  'López Fernández', 'pedro@egibide.org',  '600111004', 'visitante'),
            ('56789012E', 'María',  'Fernández Gil',   'maria@egibide.org',  '600111005', 'contratista'),
            ('67890123F', 'Juan',   'Pérez Torres',    'juan@egibide.org',   '600111006', 'empleado'),
            ('78901234G', 'Lucía',  'Gómez Díaz',      'lucia@egibide.org',  '600111007', 'empleado'),
            ('89012345H', 'Marcos', 'Ruiz Moreno',     'marcos@egibide.org', '600111008', 'visitante'),
        ]
        usuarios = []
        for dni, nombre, apellidos, email, tel, tipo in usuarios_data:
            u, _ = Usuario.objects.get_or_create(
                dni=dni,
                defaults=dict(nombre=nombre, apellidos=apellidos, email=email, telefono=tel, tipo=tipo)
            )
            usuarios.append(u)

        # Zonas
        zonas_data = [
            ('Z01', 'Entrada principal',  'Acceso general al edificio',   1, 'Planta baja'),
            ('Z02', 'Sala de servidores', 'CPD principal',                 4, 'Sótano'),
            ('Z03', 'Oficinas generales', 'Planta de trabajo habitual',    2, 'Planta 1'),
            ('Z04', 'Laboratorio I+D',    'Laboratorio de investigación',  3, 'Planta 2'),
            ('Z05', 'Almacén',            'Almacén de material',           2, 'Planta baja'),
            ('Z06', 'Sala de reuniones',  'Reuniones y presentaciones',    1, 'Planta 1'),
            ('Z07', 'Dirección',          'Despachos de dirección',        3, 'Planta 3'),
            ('Z08', 'Aparcamiento',       'Zona de vehículos',             1, 'Exterior'),
        ]
        zonas = []
        for codigo, nombre, desc, nivel, ubic in zonas_data:
            z, _ = Zona.objects.get_or_create(
                codigo=codigo,
                defaults=dict(nombre=nombre, descripcion=desc, nivel_acceso=nivel, ubicacion=ubic)
            )
            zonas.append(z)

        hoy = date.today()

        # Permisos
        permisos_data = [
            ('P001', usuarios[0], zonas[0], hoy - timedelta(30), None,               'activo'),
            ('P002', usuarios[0], zonas[2], hoy - timedelta(30), None,               'activo'),
            ('P003', usuarios[1], zonas[0], hoy - timedelta(15), hoy + timedelta(30),'activo'),
            ('P004', usuarios[2], zonas[1], hoy - timedelta(60), None,               'activo'),
            ('P005', usuarios[2], zonas[6], hoy - timedelta(60), None,               'activo'),
            ('P006', usuarios[3], zonas[0], hoy - timedelta(5),  hoy + timedelta(5), 'activo'),
            ('P007', usuarios[4], zonas[4], hoy - timedelta(90), hoy - timedelta(10),'activo'),  # caducado
            ('P008', usuarios[5], zonas[2], hoy - timedelta(10), None,               'revocado'),
        ]
        for codigo, usuario, zona, fi, ff, estado in permisos_data:
            Permiso.objects.get_or_create(
                codigo=codigo,
                defaults=dict(usuario=usuario, zona=zona, fecha_inicio=fi, fecha_fin=ff, estado=estado)
            )

        # Registros
        registros_data = [
            ('R001', usuarios[0], zonas[0], 'permitido'),
            ('R002', usuarios[0], zonas[2], 'permitido'),
            ('R003', usuarios[1], zonas[0], 'permitido'),
            ('R004', usuarios[3], zonas[1], 'denegado'),
            ('R005', usuarios[4], zonas[4], 'denegado'),
            ('R006', usuarios[5], zonas[2], 'denegado'),
            ('R007', usuarios[2], zonas[1], 'permitido'),
            ('R008', usuarios[6], zonas[0], 'denegado'),
        ]
        for codigo, usuario, zona, resultado in registros_data:
            RegistroAcceso.objects.get_or_create(
                codigo=codigo,
                defaults=dict(usuario=usuario, zona=zona, resultado=resultado)
            )

        self.stdout.write(self.style.SUCCESS('Datos de prueba cargados correctamente.'))