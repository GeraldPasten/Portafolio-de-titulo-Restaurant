from django.contrib import admin
from .models import Mesa, Inventario, Solicitud, Reserva, Receta
# Register your models here.

admin.site.register(Mesa)
admin.site.register(Inventario)
admin.site.register(Solicitud)
admin.site.register(Reserva)
admin.site.register(Receta)