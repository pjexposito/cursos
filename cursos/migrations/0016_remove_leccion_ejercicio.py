# Generated by Django 5.0.7 on 2024-08-12 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0015_transfer_images_to_imagenleccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leccion',
            name='ejercicio',
        ),
    ]
