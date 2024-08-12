# Generated by Django 5.0.7 on 2024-08-12 15:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0017_alter_leccion_explicacion_alter_leccion_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='explicacion',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='curso',
            name='fecha_creacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='curso',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercicio',
            name='fecha_creacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='leccion',
            name='fecha_creacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]