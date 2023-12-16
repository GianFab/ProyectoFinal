from django.urls import path
from Accounts.views import *


urlpatterns = [
    path('login/', login_request, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_request, name='register'),
    path('editar/', editar_request, name='editar'),
    path('editar_avatar/', editar_avatar, name='editar_avatar'),
]
