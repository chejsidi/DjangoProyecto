from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Usuario, Zona, Permiso, RegistroAcceso
from .serializers import UsuarioSerializer, ZonaSerializer, PermisoSerializer, RegistroAccesoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset            = Usuario.objects.all()
    serializer_class    = UsuarioSerializer
    permission_classes  = [IsAuthenticated]


class ZonaViewSet(viewsets.ModelViewSet):
    queryset           = Zona.objects.all()
    serializer_class   = ZonaSerializer
    permission_classes = [IsAuthenticated]


class PermisoViewSet(viewsets.ModelViewSet):
    queryset           = Permiso.objects.select_related('usuario', 'zona').all()
    serializer_class   = PermisoSerializer
    permission_classes = [IsAuthenticated]


class RegistroAccesoViewSet(viewsets.ModelViewSet):
    queryset           = RegistroAcceso.objects.select_related('usuario', 'zona').all()
    serializer_class   = RegistroAccesoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Calcula resultado automáticamente igual que la vista web."""
        usuario = serializer.validated_data['usuario']
        zona    = serializer.validated_data['zona']

        permiso = Permiso.objects.filter(usuario=usuario, zona=zona).first()
        resultado = 'permitido' if (permiso and permiso.esta_vigente()) else 'denegado'

        serializer.save(resultado=resultado)