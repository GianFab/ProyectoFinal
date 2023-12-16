from django.contrib import admin
from Clama.models import Producto, Calzado, Camiseta, Pantalon, Usuario

# Register your models here.

admin.site.register(Producto)
admin.site.register(Calzado)
admin.site.register(Camiseta)
admin.site.register(Pantalon)
admin.site.register(Usuario)