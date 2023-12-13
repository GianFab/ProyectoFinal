from django.urls import path
from Clama.views.calzado_views import *
from Clama.views.producto_views import *
from Clama.views.pantalon_views import *
from Clama.views.camiseta_views import *
from Clama.views.usuario_views import *

urlpatterns = [
    path('calzado/', lista_calzados),
]
