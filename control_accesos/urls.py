from django.urls import path
from . import views

app_name = "control_accesos"

urlpatterns = [
    path("", views.panel, name="panel"),
    # Usuarios
    path("usuarios/", views.usuario_lista, name="usuario_lista"),
    path("usuarios/nuevo/", views.usuario_crear, name="usuario_crear"),
    path("usuarios/<int:pk>/", views.usuario_detalle, name="usuario_detalle"),
    path("usuarios/<int:pk>/editar/", views.usuario_editar, name="usuario_editar"),
    path(
        "usuarios/<int:pk>/eliminar/", views.usuario_eliminar, name="usuario_eliminar"
    ),
]
