from django.db import models
from django.utils import timezone
from apps.usuario.models import Usuario
from django.db.models.signals import post_save, pre_save, post_delete, m2m_changed
from datetime import datetime 
# Create your models here.


class Mesa(models.Model):
	nro_mesa = models.CharField('Mesa', max_length= 5, unique=True,  blank= False, null = False)
	disponible = models.BooleanField('Disponible', default = True)   

	class Meta:
		verbose_name = 'Mesa'
		verbose_name_plural = 'Mesas'
		ordering = ['nro_mesa']

	def natural_key(self):
		return f'{self.nro_mesa}'

	def __str__(self):
		return self.nro_mesa

class Inventario(models.Model):
	id = models.AutoField(primary_key= True)
	producto = models.CharField('Nombre producto', max_length = 255, blank = False, null = False)
	stock = models.PositiveIntegerField('Cantidad o Stock', default= 1)
	nombre_encargado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	fecha_ult_revision = models.DateField('Fecha ultima revision', default = timezone.now)
	disponibilidad_stock = models.BooleanField('Hay stock', default = True)  

	class Meta:
		verbose_name = 'Inventario'
		verbose_name_plural = 'Inventarios'
		ordering= ['producto']

	def __str__(self):
		return self.producto

	def natural_key(self):
		return self.producto

class Solicitud(models.Model):
	id= models.AutoField(primary_key= True)
	insumo = models.CharField('Nombre insumo', max_length = 255, blank = False, null = False)
	cantidad = models.PositiveIntegerField('cantidad insumo', default = 1)
	fecha_solicitud = models.DateField('Fecha de Solicitud', default = timezone.now)
	estado = models.BooleanField('estado', default = True)
	nombre_solicitante = models.CharField('nombre_solicitante', max_length = 255, blank = False, null = False)

	class Meta:
		verbose_name = 'Solicitud'
		verbose_name_plural = 'Solicitudes'
		ordering = ['id']

	def __str__(self):
		return self.insumo

	def natural_key(self):
		return self.insumo			
					
class Reserva(models.Model):

	cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	fecha_creacion = models.DateTimeField('Inicio', auto_now = False,default = timezone.now)
	fecha_cierre= models.DateTimeField('Cierre', auto_now=False, null = True, blank = True,default = timezone.now)
	mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
	notas = models.TextField('notas', null = True, blank = True)
	estado = models.BooleanField(default = True, verbose_name = 'Estado')

	class Meta:
		verbose_name = 'Reserva'
		verbose_name_plural = 'Reservas'

	def __str__(self):
		return f'Reserva el cliente {self.cliente} para la mesa {self.mesa}'


class Receta(models.Model):

	titulo = models.CharField('Titulo',max_length=255, blank= False, null=False)
	descripcion = models.TextField('Descripción',null= False, blank= False)
	ingredientes = models.TextField('Ingredientes', null= False, blank= False )
	instrucciones = models.TextField('Instrucciones', null= False, blank= False)
	imagen = models.ImageField('Imagen Receta', upload_to='receta/', max_length=200, null=False)
	precio = models.PositiveIntegerField('Precio',default= 0)
	disponible = models.BooleanField('Disponible', default = True)
	

	class Meta:
		verbose_name= 'Receta'
		verbose_name_plural= 'Recetas'

	def __str__(self):
		return self.titulo

class Orden(models.Model):

	mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
	platillos = models.TextField('Platillos', null= False)
	prioridad = models.CharField('Prioridad',max_length=255 ,null= False)
	estado = models.BooleanField(default = True, verbose_name = 'Estado')

	class Meta:
		verbose_name= 'Orden'
		verbose_name_plural = 'Ordenes'

	def __str__(self):
		return self.mesa


# Principio
class UserOrder(models.Model):
	username = models.CharField(max_length=200) #who placed the order
	order = models.TextField() #this will be a string representation of the cart from localStorage
	price = models.PositiveIntegerField(default=0) #how much was the order
	time_of_order = models.DateTimeField(default=datetime.now, blank=True)
	delivered = models.BooleanField()

	def __str__(self):
		#overriding the string method to get a good representation of it in string format
		return f"Order placed by  : {self.username} on {self.time_of_order.date()} at {self.time_of_order.time().strftime('%H:%M:%S')}"

class SavedCarts(models.Model):
	username = models.CharField(max_length=200, primary_key=True)
	cart = models.TextField() #this will be a string representation of the cart from localStorage

	def __str__(self):
		#overriding the string method to get a good representation of it in string format
		return f"Saved cart for {self.username}"




# Final


def disponibilidad_mesa(sender,instance,**kwargs):

	mesa = instance.mesa
	if mesa.disponible == True:
		mesa.disponible = False
		mesa.save()


def disponibilidad_mesa_reserva(sender,instance,**kwargs):
	reserva = instance.mesa
	if reserva.disponible == False:
		reserva.disponible = True
		reserva.save()


post_save.connect(disponibilidad_mesa,sender = Reserva)
#m2m_changed.connect(disponibilidad_mesa_reserva, sender = Reserva)
