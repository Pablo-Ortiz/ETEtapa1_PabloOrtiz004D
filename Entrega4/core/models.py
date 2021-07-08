from django.db import models

# Create your models here.

class Pais(models.Model):
	idPais = models.IntegerField(primary_key=True)
	nombrePais = models.CharField(max_length=50)

	def __str__(self):
		return self.nombrePais

class Usuario(models.Model):
    RutUsuario = models.CharField(max_length=10, primary_key=True, verbose_name='Rut del Usuario')
    nombreCom = models.CharField(max_length=50, verbose_name='Nombre completo del usuario')
    telefono = models.CharField(max_length=12, verbose_name='Telefono del usuario')
    direccion = models.CharField(max_length=50, verbose_name='Dirección')
    email = models.CharField(max_length=70, verbose_name='Mail')
    image = models.ImageField(upload_to='images/', null=True)
    passw = models.CharField(max_length=8, null=True, blank=False)
    idPais = models.ForeignKey('Pais', on_delete=models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return self.RutUsuario