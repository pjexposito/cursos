# Generated by Django 5.0.7 on 2024-08-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0018_alter_curso_explicacion_alter_curso_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarioleccion',
            name='puntos_obtenidos',
            field=models.SmallIntegerField(default=10),
            preserve_default=False,
        ),
    ]
