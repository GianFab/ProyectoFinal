from django.contrib.auth.models import User
from django.db import models


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    pagina = models.URLField(blank=True, null=True)

