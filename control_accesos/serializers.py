from rest_framework import serializers
from .models import Usuario, Zona, Permiso, RegistroAcceso


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Usuario
        fields = ['id', 'dni', 'nombre', 'apellidos', 'email', 'telefono', 'tipo']


class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Zona
        fields = ['id', 'codigo', 'nombre', 'descripcion', 'nivel_acceso', 'ubicacion']


class PermisoSerializer(serializers.ModelSerializer):
    esta_vigente = serializers.SerializerMethodField()

    class Meta:
        model  = Permiso
        fields = ['id', 'codigo', 'usuario', 'zona', 'fecha_inicio', 'fecha_fin', 'estado', 'esta_vigente']

    def get_esta_vigente(self, obj):
        return obj.esta_vigente()


class RegistroAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = RegistroAcceso
        fields = ['id', 'codigo', 'fecha', 'hora', 'usuario', 'zona', 'resultado', 'observaciones']
        read_only_fields = ['fecha', 'hora', 'resultado']