from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm


def panel(request):
    return render(request, "control_accesos/panel.html")


# --- Usuarios ---


def usuario_lista(request):
    usuarios = Usuario.objects.all()
    return render(request, "control_accesos/usuario_lista.html", {"usuarios": usuarios})


def usuario_detalle(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, "control_accesos/usuario_detalle.html", {"usuario": usuario})


def usuario_crear(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado correctamente.")
            return redirect("control_accesos:usuario_lista")
    else:
        form = UsuarioForm()
    return render(
        request,
        "control_accesos/usuario_form.html",
        {"form": form, "titulo": "Nuevo usuario"},
    )


def usuario_editar(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado correctamente.")
            return redirect("control_accesos:usuario_lista")
    else:
        form = UsuarioForm(instance=usuario)
    return render(
        request,
        "control_accesos/usuario_form.html",
        {"form": form, "titulo": "Editar usuario"},
    )


def usuario_eliminar(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        usuario.delete()
        messages.success(request, "Usuario eliminado correctamente.")
        return redirect("control_accesos:usuario_lista")
    return render(
        request, "control_accesos/usuario_confirmar_eliminar.html", {"usuario": usuario}
    )
