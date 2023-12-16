from django.urls import path
from Accounts.views import *


urlpatterns = [
    path('login/', login_request, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_request, name='register'),
    path('editar_avatar/', editar_avatar, name='editar_avatar'),
    path('editar_usuario/', editar_request, name='editar'),
]
