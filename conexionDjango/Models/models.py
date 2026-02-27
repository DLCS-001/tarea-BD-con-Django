from django.db import models


class Usuarios(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'usuarios'
        managed = False

    def __str__(self):
        return self.nombres


class Autores(models.Model):
    id_autores = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)

    class Meta:
        db_table = 'autores'
        managed = False

    def __str__(self):
        return self.nombres


class Categorias(models.Model):
    id_Categorias = models.AutoField(primary_key=True, db_column='id_Categorias')
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'Categorias'
        managed = False

    def __str__(self):
        return self.nombre


class Libros(models.Model):
    id_Libros = models.AutoField(primary_key=True, db_column='id_Libros')
    titulo = models.CharField(max_length=45)
    autores_id_autores = models.ForeignKey(
        'Autores',
        on_delete=models.CASCADE,
        db_column='autores_id_autores'
    )
    Categorias_id_Categorias = models.ForeignKey(
        'Categorias',
        on_delete=models.CASCADE,
        db_column='Categorias_id_Categorias'
    )

    class Meta:
        db_table = 'Libros'
        managed = False

    def __str__(self):
        return self.titulo


class Prestamos(models.Model):
    id_Prestamos = models.AutoField(primary_key=True, db_column='id_Prestamos')
    fecha = models.CharField(max_length=100, null=True, blank=True)
    usuarios_id_usuarios = models.ForeignKey(
        'Usuarios',
        on_delete=models.CASCADE,
        db_column='usuarios_id_usuarios'
    )
    Libros_id_Libros = models.ForeignKey(
        'Libros',
        on_delete=models.CASCADE,
        db_column='Libros_id_Libros'
    )

    class Meta:
        db_table = 'Prestamos'
        managed = False

    def __str__(self):
        return f"Préstamo {self.id_Prestamos} - {self.fecha}"