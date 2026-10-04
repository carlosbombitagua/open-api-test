from django.db import models

# Create your models here.

class Categoria (models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id Categoria')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria

class Comida(models.Model):
    marca = models.CharField(max_length=20, primary_key=True, verbose_name='Marca')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    tamanno = models.CharField(max_length=4, verbose_name='Tamaño')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.marca

class Usuario(models.Model):
    idUser = models.IntegerField(primary_key=True, verbose_name='Id usuario')
    nombreUser = models.CharField(max_length=50, verbose_name='Nombre usuario')
    
    def __str__(self):
        return self.nombreUser

class Cliente(models.Model):
    rut = models.CharField(max_length=13, primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    gmail = models.CharField(max_length=40, verbose_name='Gmail')
    telefono = models.CharField(max_length=10, verbose_name='Telefono')
    direccion = models.CharField(max_length=40, verbose_name='Direccion')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut
