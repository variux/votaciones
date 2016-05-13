from __future__ import unicode_literals

from django.db import models

# Create your models here.




class Partido(models.Model):
	nombre = models.CharField(max_length=255)
	bandera = models.ImageField()
	slogan = models.CharField(max_length = 200)
	cantidad_votos = models.IntegerField(null=True, blank=True) 


class Estudiante(models.Model):
	nombre = models.CharField(max_length = 255)
	cedula = models.IntegerField()
	do_vote = models.BooleanField(default=False)
	gender = models.IntegerField(null=True)


class Mesa(models.Model):
	titulo = models.CharField(max_length = 255)
	is_available = models.BooleanField()


