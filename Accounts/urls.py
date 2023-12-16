from django.contrib.auth.views import LogoutView
from django.urls import path
from Accounts.views import *


urlpatterns = [
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name="Accounts/logout.html"), name='logout'),
]
