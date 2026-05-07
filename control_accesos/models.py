from django.db import models
from django.utils import timezone

# ── Usuario ──────────────────────────────────────────────────────────────────

TIPO_USUARIO = [
    ("empleado", "Empleado"),
    ("visitante", "Visitante"),
    ("contratista", "Contratista"),
    ("admin", "Administrador"),
]


class Usuario(models.Model):
    dni = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO, default="empleado")

    def __str__(self):
        return f"{self.apellidos}, {self.nombre}"


# ── Zona ──────────────────────────────────────────────────────────────────────

NIVEL_ACCESO = [
    (1, "Nivel 1 – Público"),
    (2, "Nivel 2 – Restringido"),
    (3, "Nivel 3 – Confidencial"),
    (4, "Nivel 4 – Alta seguridad"),
]


class Zona(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    nivel_acceso = models.IntegerField(choices=NIVEL_ACCESO, default=1)
    ubicacion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.codigo} – {self.nombre}"


# ── Permiso (many-to-many Usuario ↔ Zona con datos propios) ──────────────────

ESTADO_PERMISO = [
    ("activo", "Activo"),
    ("caducado", "Caducado"),
    ("revocado", "Revocado"),
]


class Permiso(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="permisos"
    )
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name="permisos")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_PERMISO, default="activo")

    def esta_vigente(self):
        """Devuelve True si el permiso cubre hoy y está activo."""
        hoy = timezone.now().date()
        if self.estado != "activo":
            return False
        if self.fecha_fin and self.fecha_fin < hoy:
            return False
        return hoy >= self.fecha_inicio

    def __str__(self):
        return f"{self.codigo} | {self.usuario} → {self.zona}"


# ── Registro de Acceso ────────────────────────────────────────────────────────

RESULTADO_ACCESO = [
    ("permitido", "Permitido"),
    ("denegado", "Denegado"),
]


class RegistroAcceso(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="registros"
    )
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name="registros")
    resultado = models.CharField(max_length=20, choices=RESULTADO_ACCESO)
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ["-fecha", "-hora"]

    def __str__(self):
        return f"{self.codigo} | {self.usuario} → {self.zona} [{self.resultado}]"
