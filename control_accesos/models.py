from django.db import models


class Usuario(models.Model):
    TIPO_CHOICES = [
        ("empleado", "Empleado"),
        ("visitante", "Visitante"),
        ("administrador", "Administrador"),
        ("contratista", "Contratista"),
    ]

    dni = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default="empleado")

    class Meta:
        ordering = ["apellidos", "nombre"]

    def __str__(self):
        return f"{self.apellidos}, {self.nombre} ({self.dni})"


class Zona(models.Model):
    NIVEL_CHOICES = [
        (1, "Nivel 1 - Público"),
        (2, "Nivel 2 - Empleados"),
        (3, "Nivel 3 - Restringido"),
        (4, "Nivel 4 - Alta Seguridad"),
    ]

    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    nivel_acceso = models.IntegerField(choices=NIVEL_CHOICES, default=1)
    ubicacion = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["nivel_acceso", "nombre"]

    def __str__(self):
        return f"[{self.codigo}] {self.nombre}"


class Permiso(models.Model):
    ESTADO_CHOICES = [
        ("activo", "Activo"),
        ("caducado", "Caducado"),
        ("revocado", "Revocado"),
        ("pendiente", "Pendiente"),
    ]

    codigo = models.CharField(max_length=20, unique=True)
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="permisos"
    )
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name="permisos")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default="activo")

    class Meta:
        ordering = ["-fecha_inicio"]

    def __str__(self):
        return f"{self.codigo} - {self.usuario} → {self.zona}"

    def esta_vigente(self):
        from django.utils import timezone

        hoy = timezone.now().date()
        if self.estado != "activo":
            return False
        if self.fecha_fin and hoy > self.fecha_fin:
            return False
        if hoy < self.fecha_inicio:
            return False
        return True


class RegistroAcceso(models.Model):
    RESULTADO_CHOICES = [
        ("permitido", "Acceso Permitido"),
        ("denegado", "Acceso Denegado"),
        ("sin_permiso", "Sin Permiso"),
        ("caducado", "Permiso Caducado"),
    ]

    codigo = models.CharField(max_length=20, unique=True)
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="registros"
    )
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name="registros")
    fecha = models.DateField()
    hora = models.TimeField()
    resultado = models.CharField(max_length=20, choices=RESULTADO_CHOICES)
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ["-fecha", "-hora"]

    def __str__(self):
        return f"{self.codigo} | {self.fecha} {self.hora} | {self.resultado}"
