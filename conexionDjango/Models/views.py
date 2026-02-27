from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuarios, Autores, Categorias, Libros, Prestamos
from .forms import UsuarioForm, AutorForm, CategoriaForm, LibroForm, PrestamoForm

# pagina de inicio
def home(request):
    return render(request, 'gestion/home.html', {
        'titulo': 'Sistema de Biblioteca'
    })

# Vistas para Usuarios
def lista_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'gestion/usuarios/lista.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'gestion/usuarios/formulario.html', {'form': form, 'accion': 'Crear'})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'gestion/usuarios/formulario.html', {'form': form, 'accion': 'Editar'})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente.')
        return redirect('lista_usuarios')
    return render(request, 'gestion/usuarios/eliminar.html', {'usuario': usuario})

# Vistas para Autores
def lista_autores(request):
    autores = Autores.objects.all()
    return render(request, 'gestion/autores/lista.html', {'autores': autores})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado exitosamente.')
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'gestion/autores/formulario.html', {'form': form, 'accion': 'Crear'})

def editar_autor(request, pk):
    autor = get_object_or_404(Autores, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor actualizado exitosamente.')
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'gestion/autores/formulario.html', {'form': form, 'accion': 'Editar'})

def eliminar_autor(request, pk):
    autor = get_object_or_404(Autores, pk=pk)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, 'Autor eliminado exitosamente.')
        return redirect('lista_autores')
    return render(request, 'gestion/autores/eliminar.html', {'autor': autor})

# Vistas para Categorías
def lista_categorias(request):
    categorias = Categorias.objects.all()
    return render(request, 'gestion/categorias/lista.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'gestion/categorias/formulario.html', {'form': form, 'accion': 'Crear'})

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categorias, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'gestion/categorias/formulario.html', {'form': form, 'accion': 'Editar'})

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categorias, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada exitosamente.')
        return redirect('lista_categorias')
    return render(request, 'gestion/categorias/eliminar.html', {'categoria': categoria})

# Vistas para Libros
def lista_libros(request):
    libros = Libros.objects.all()
    return render(request, 'gestion/libros/lista.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado exitosamente.')
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'gestion/libros/formulario.html', {'form': form, 'accion': 'Crear'})

def editar_libro(request, pk):
    libro = get_object_or_404(Libros, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado exitosamente.')
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'gestion/libros/formulario.html', {'form': form, 'accion': 'Editar'})

def eliminar_libro(request, pk):
    libro = get_object_or_404(Libros, pk=pk)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado exitosamente.')
        return redirect('lista_libros')
    return render(request, 'gestion/libros/eliminar.html', {'libro': libro})

# Vistas para Préstamos
def lista_prestamos(request):
    prestamos = Prestamos.objects.all()
    return render(request, 'gestion/prestamos/lista.html', {'prestamos': prestamos})

def crear_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Préstamo creado exitosamente.')
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm()
    return render(request, 'gestion/prestamos/formulario.html', {'form': form, 'accion': 'Crear'})

def editar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamos, pk=pk)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Préstamo actualizado exitosamente.')
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'gestion/prestamos/formulario.html', {'form': form, 'accion': 'Editar'})

def eliminar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamos, pk=pk)
    if request.method == 'POST':
        prestamo.delete()
        messages.success(request, 'Préstamo eliminado exitosamente.')
        return redirect('lista_prestamos')
    return render(request, 'gestion/prestamos/eliminar.html', {'prestamo': prestamo})