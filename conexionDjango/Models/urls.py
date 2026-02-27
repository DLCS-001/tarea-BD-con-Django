from django.urls import path
from . import views

urlpatterns = [
    #inico
path('', views.home, name='home'),

    # Usuarios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),

    # Autores
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),
    path('autores/eliminar/<int:pk>/', views.eliminar_autor, name='eliminar_autor'),

    # Categorías
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),

    # Libros
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/editar/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),

    # Préstamos
    path('prestamos/', views.lista_prestamos, name='lista_prestamos'),
    path('prestamos/crear/', views.crear_prestamo, name='crear_prestamo'),
    path('prestamos/editar/<int:pk>/', views.editar_prestamo, name='editar_prestamo'),
    path('prestamos/eliminar/<int:pk>/', views.eliminar_prestamo, name='eliminar_prestamo'),
]