from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register('usuarios',  api_views.UsuarioViewSet)
router.register('zonas',     api_views.ZonaViewSet)
router.register('permisos',  api_views.PermisoViewSet)
router.register('registros', api_views.RegistroAccesoViewSet)

urlpatterns = router.urls