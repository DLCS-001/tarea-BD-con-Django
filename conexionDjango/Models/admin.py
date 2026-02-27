from django.contrib import admin
from .models import Usuarios, Autores, Categorias, Libros, Prestamos

# Registrar los modelos en el admin
admin.site.register(Usuarios)
admin.site.register(Autores)
admin.site.register(Categorias)
admin.site.register(Libros)
admin.site.register(Prestamos)