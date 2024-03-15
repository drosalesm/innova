from django.contrib import admin
from .models import *
# Register your models here.



class OrdenesEmitidasAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ordenes_emitidas._meta.fields]  # Muestra todos los campos del modelo
    list_display_links = ['id']  # Vincula el campo 'id' en la lista de instancias



admin.site.register(ordenes_emitidas,OrdenesEmitidasAdmin)



admin.site.register(encabezadoFactura)

