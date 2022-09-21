from django.db import models

# Create your models here.

class Buzos(models.Model):
    color: models.CharField(max_length=40)
    talle: models.CharField(max_length=40)
    marca: models.CharField(max_length=40)

class Remeras(models.Model):
    color: models.CharField(max_length=40)
    talle: models.CharField(max_length=40)
    marca: models.CharField(max_length=40)

class Pantalones(models.Model):
    color: models.CharField(max_length=40)
    talle: models.CharField(max_length=40)
    marca: models.CharField(max_length=40)