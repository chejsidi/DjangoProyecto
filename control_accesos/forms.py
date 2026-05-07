from django import forms
from .models import Usuario
from .models import Zona

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