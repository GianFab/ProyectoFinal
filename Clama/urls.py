from django.urls import path
from Clama.views.calzado_views import *
from Clama.views.producto_views import *
from Clama.views.pantalon_views import *
from Clama.views.camiseta_views import *
from Clama.views.usuario_views import *

urlpatterns = [
    path('calzados/', lista_calzados, name='calzados'),
    path('calzado/<int:calzado_id>/', detalle_calzado),
    path('buscar_calzado/', busqueda_calzado),
    path('crear_calzado/', crear_calzado),
    path('actualizar_calzado/<int:calzado_id>/', editar_calzado, name='actualizar_calzado'),
    path('eliminar_calzado/<int:calzado_id>/', eliminar_calzado, name='eliminar_calzado'),
    path('camiseta/', lista_camisetas),
    path('principal/', probando),
]
