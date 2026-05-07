from django import forms
from .models import Usuario
from .models import Zona
from .models import Permiso

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["dni", "nombre", "apellidos", "email", "telefono", "tipo"]
        widgets = {
            "dni": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellidos": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "tipo": forms.Select(attrs={"class": "form-select"}),
        }


class ZonaForm(forms.ModelForm):
    class Meta:
        model  = Zona
        fields = ['codigo', 'nombre', 'descripcion', 'nivel_acceso', 'ubicacion']
        widgets = {
            'codigo':       forms.TextInput(attrs={'class': 'form-control'}),
            'nombre':       forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':  forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nivel_acceso': forms.Select(attrs={'class': 'form-select'}),
            'ubicacion':    forms.TextInput(attrs={'class': 'form-control'}),
        }

class PermisoForm(forms.ModelForm):
    class Meta:
        model  = Permiso
        fields = ['codigo', 'usuario', 'zona', 'fecha_inicio', 'fecha_fin', 'estado']
        widgets = {
            'codigo':       forms.TextInput(attrs={'class': 'form-control'}),
            'usuario':      forms.Select(attrs={'class': 'form-select'}),
            'zona':         forms.Select(attrs={'class': 'form-select'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin':    forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado':       forms.Select(attrs={'class': 'form-select'}),
        }