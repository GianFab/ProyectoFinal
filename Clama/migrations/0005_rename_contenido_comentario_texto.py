# Generated by Django 5.0 on 2023-12-16 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clama', '0004_producto_usuario_comentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='contenido',
            new_name='texto',
        ),
    ]
