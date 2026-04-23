# Egibide Access Control

Sistema de gestión de accesos a instalaciones para **Egibide Access Control S.L.**
Permite registrar qué personas pueden entrar a determinadas zonas y dejar constancia de cada intento de acceso, distinguiendo entre accesos autorizados, denegados o con permisos caducados.

## Repositorio GitHub

https://github.com/chejsidi/DjangoProyecto

## Requisitos

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)

## Instalación y puesta en marcha

```bash
# Clonar el repositorio
git clone https://github.com/chejsidi/DjangoProyecto.git
cd DjangoProyecto

# Instalar dependencias
uv sync

# Aplicar migraciones
uv run python manage.py migrate

# Crear superusuario (para el panel de administración)
uv run python manage.py createsuperuser

# Arrancar el servidor
uv run python manage.py runserver
```

Accede a la aplicación en `http://localhost:8000` y al panel de administración en `http://localhost:8000/admin`.

## Modelos principales

| Modelo | Descripción |
|---|---|
| `Usuario` | DNI, nombre, apellidos, email, teléfono, tipo |
| `Zona` | Código, nombre, descripción, nivel de acceso, ubicación |
| `Permiso` | Relaciona Usuario↔Zona con fecha inicio, fin y estado |
| `RegistroAcceso` | Evento real de acceso con fecha, hora y resultado |

## Funcionalidades

- [ ] Gestión de usuarios: alta, listado, detalle, actualización y baja
- [ ] Gestión de zonas: alta, listado, detalle, actualización y baja
- [ ] Gestión de permisos: alta, listado, detalle, actualización y baja
- [ ] Registro de accesos: alta, listado y detalle
- [ ] Consulta de accesos por usuario, fecha o zona
- [ ] Validación de acceso autorizado o denegado
- [ ] Panel de accesos recientes
- [ ] Histórico de permisos caducados

## Incidencias conocidas

Ninguna actualmente.