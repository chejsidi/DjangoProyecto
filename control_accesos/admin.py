from django.contrib import admin
from .models import Usuario, Zona, Permiso, RegistroAcceso


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['dni', 'apellidos', 'nombre', 'email', 'tipo']
    search_fields = ['dni', 'nombre', 'apellidos', 'email']
    list_filter = ['tipo']


@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'nivel_acceso', 'ubicacion']
    list_filter = ['nivel_acceso']
    search_fields = ['codigo', 'nombre']


@admin.register(Permiso)
class PermisoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'usuario', 'zona', 'fecha_inicio', 'fecha_fin', 'estado']
    list_filter = ['estado']
    search_fields = ['codigo']


@admin.register(RegistroAcceso)
class RegistroAccesoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'usuario', 'zona', 'fecha', 'hora', 'resultado']
    list_filter = ['resultado', 'fecha']
    search_fields = ['codigo']