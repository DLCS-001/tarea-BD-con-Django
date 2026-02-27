from django import forms
from .models import Usuarios, Autores, Categorias, Libros, Prestamos


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombres', 'correo']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
        }


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autores
        fields = ['nombres']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del autor'}),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
        }


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo', 'autores_id_autores', 'Categorias_id_Categorias']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del libro'}),
            'autores_id_autores': forms.Select(attrs={'class': 'form-control'}),
            'Categorias_id_Categorias': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['autores_id_autores'].label = "Autor"
        self.fields['Categorias_id_Categorias'].label = "Categoría"


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamos
        fields = ['fecha', 'usuarios_id_usuarios', 'Libros_id_Libros']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'usuarios_id_usuarios': forms.Select(attrs={'class': 'form-control'}),
            'Libros_id_Libros': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuarios_id_usuarios'].label = "Usuario"
        self.fields['Libros_id_Libros'].label = "Libro"