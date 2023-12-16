from django.urls import path
from Clama.views.calzado_views import *
from Clama.views.comentario_views import *
from Clama.views.producto_views import *
from Clama.views.pantalon_views import *
from Clama.views.camiseta_views import *
from Clama.views.usuario_views import *


urlpatterns = [
    path('calzados/', ListaCalzados.as_view(), name='calzados'),
    path('calzado/<int:calzado_id>/', DetalleCalzado.as_view(), name='detalle_calzado'),
    path('buscar_calzado/', BusquedaCalzado.as_view()),
    path('crear_calzado/', CrearCalzado.as_view()),
    path('actualizar_calzado/<int:calzado_id>/', EditarCalzado.as_view(), name='actualizar_calzado'),
    path('eliminar_calzado/<int:calzado_id>/', EliminarCalzado.as_view(), name='eliminar_calzado'),

    path('camisetas/', ListaCamisetas.as_view(), name='camisetas'),
    path('camiseta/<int:camiseta_id>/', DetalleCamiseta.as_view(), name='detalle_camiseta'),
    path('buscar_camiseta/', BusquedaCamiseta.as_view()),
    path('crear_camiseta/', CrearCamiseta.as_view()),
    path('actualizar_camiseta/<int:camiseta_id>/', EditarCamiseta.as_view(), name='actualizar_camiseta'),
    path('eliminar_camiseta/<int:camiseta_id>/', EliminarCamiseta.as_view(), name='eliminar_camiseta'),

    path('pantalones/', ListaPantalones.as_view(), name='pantalones'),
    path('pantalon/<int:pantalon_id>/', DetallePantalon.as_view(), name='detalle_pantalon'),
    path('buscar_pantalon/', BusquedaPantalon.as_view()),
    path('crear_pantalon/', CrearPantalon.as_view()),
    path('actualizar_pantalon/<int:pantalon_id>/', EditarPantalon.as_view(), name='actualizar_pantalon'),
    path('eliminar_pantalon/<int:pantalon_id>/', EliminarPantalon.as_view(), name='eliminar_pantalon'),

    path('agregar_comentario_cl/<int:calzado_id>/', AgregarComentarioCalzado.as_view(), name='agregar_comentario_calzado'),
    path('agregar_comentario_p/<int:pantalon_id>/', AgregarComentarioPantalon.as_view(), name='agregar_comentario_pantalon'),
    path('agregar_comentario_cm/<int:camiseta_id>/', AgregarComentarioCamiseta.as_view(), name='agregar_comentario_camiseta'),
    
    path('principal/', ListaProductos.as_view(), name='principal'),
]
