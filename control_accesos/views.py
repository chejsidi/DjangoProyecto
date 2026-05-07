from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm
from .models import Zona
from .forms  import ZonaForm
from .models import Permiso
from .forms  import PermisoForm
from .models import RegistroAcceso
from .forms  import RegistroAccesoForm

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

# --- Zonas ---

def zona_lista(request):
    zonas = Zona.objects.all()
    return render(request, 'control_accesos/zona_lista.html', {'zonas': zonas})

def zona_detalle(request, pk):
    zona = get_object_or_404(Zona, pk=pk)
    return render(request, 'control_accesos/zona_detalle.html', {'zona': zona})

def zona_crear(request):
    if request.method == 'POST':
        form = ZonaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Zona creada correctamente.')
            return redirect('control_accesos:zona_lista')
    else:
        form = ZonaForm()
    return render(request, 'control_accesos/zona_form.html', {'form': form, 'titulo': 'Nueva zona'})

def zona_editar(request, pk):
    zona = get_object_or_404(Zona, pk=pk)
    if request.method == 'POST':
        form = ZonaForm(request.POST, instance=zona)
        if form.is_valid():
            form.save()
            messages.success(request, 'Zona actualizada correctamente.')
            return redirect('control_accesos:zona_lista')
    else:
        form = ZonaForm(instance=zona)
    return render(request, 'control_accesos/zona_form.html', {'form': form, 'titulo': 'Editar zona'})

def zona_eliminar(request, pk):
    zona = get_object_or_404(Zona, pk=pk)
    if request.method == 'POST':
        zona.delete()
        messages.success(request, 'Zona eliminada.')
        return redirect('control_accesos:zona_lista')
    return render(request, 'control_accesos/zona_confirmar_eliminar.html', {'zona': zona})

# --- Permisos ---

def permiso_lista(request):
    permisos = Permiso.objects.select_related('usuario', 'zona').all()
    return render(request, 'control_accesos/permiso_lista.html', {'permisos': permisos})

def permiso_detalle(request, pk):
    permiso = get_object_or_404(Permiso, pk=pk)
    return render(request, 'control_accesos/permiso_detalle.html', {'permiso': permiso})

def permiso_crear(request):
    if request.method == 'POST':
        form = PermisoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Permiso creado correctamente.')
            return redirect('control_accesos:permiso_lista')
    else:
        form = PermisoForm()
    return render(request, 'control_accesos/permiso_form.html', {'form': form, 'titulo': 'Nuevo permiso'})

def permiso_editar(request, pk):
    permiso = get_object_or_404(Permiso, pk=pk)
    if request.method == 'POST':
        form = PermisoForm(request.POST, instance=permiso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Permiso actualizado.')
            return redirect('control_accesos:permiso_lista')
    else:
        form = PermisoForm(instance=permiso)
    return render(request, 'control_accesos/permiso_form.html', {'form': form, 'titulo': 'Editar permiso'})

def permiso_eliminar(request, pk):
    permiso = get_object_or_404(Permiso, pk=pk)
    if request.method == 'POST':
        permiso.delete()
        messages.success(request, 'Permiso eliminado.')
        return redirect('control_accesos:permiso_lista')
    return render(request, 'control_accesos/permiso_confirmar_eliminar.html', {'permiso': permiso})


# --- Registros de acceso ---

def registro_lista(request):
    registros = RegistroAcceso.objects.select_related('usuario', 'zona').all()

    usuario_id = request.GET.get('usuario')
    zona_id    = request.GET.get('zona')
    fecha      = request.GET.get('fecha')

    if usuario_id:
        registros = registros.filter(usuario_id=usuario_id)
    if zona_id:
        registros = registros.filter(zona_id=zona_id)
    if fecha:
        registros = registros.filter(fecha=fecha)

    return render(request, 'control_accesos/registro_lista.html', {
        'registros':      registros,
        'usuarios':       Usuario.objects.all(),
        'zonas':          Zona.objects.all(),
        'filtro_usuario': usuario_id,
        'filtro_zona':    zona_id,
        'filtro_fecha':   fecha,
    })

def registro_detalle(request, pk):
    registro = get_object_or_404(RegistroAcceso, pk=pk)
    return render(request, 'control_accesos/registro_detalle.html', {'registro': registro})

def registro_crear(request):
    if request.method == 'POST':
        form = RegistroAccesoForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)

            # ── Validación automática 
            permiso = Permiso.objects.filter(
                usuario=registro.usuario,
                zona=registro.zona,
            ).first()

            if permiso and permiso.esta_vigente():
                registro.resultado = 'permitido'
            else:
                registro.resultado = 'denegado'

            registro.save()
            messages.success(request, f'Acceso registrado: {registro.get_resultado_display()}.')
            return redirect('control_accesos:registro_lista')
    else:
        form = RegistroAccesoForm()
    return render(request, 'control_accesos/registro_form.html', {'form': form, 'titulo': 'Registrar acceso'})