from django.db import models

# Create your models here.

class Buzos(models.Model):
    color: models.CharField(max_length=40)
    talle: models.CharField(max_length=40)
    marca: models.CharField(max_length=40)

    def __str__(self):
        return f"Color:{self.color} - Talle:{self.talle} - Marca:{self.marca}"

class Remeras(models.Model):
    color: models.CharField(max_length=40)
    talle: models.CharField(max_length=40)
    marca: models.CharField(max_length=40)

    def __str__(self):
        return f"Color:{self.color} - Talle:{self.talle} - Marca:{self.marca}"

class Pantalones(models.Model):
    color: models.CharField(max_length=40)
    talle: models.CharField(max_length=40)
    marca: models.CharField(max_length=40)

    def __str__(self):
        return f"Color:{self.color} - Talle:{self.talle} - Marca:{self.marca}"

class Usuario(models.Model): 
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre:{self.nombre} - Apellido:{self.apellido} - Email:{self.email}"