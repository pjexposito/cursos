# Generated by Django 5.0.7 on 2024-08-22 11:10

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0020_pregunta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default='Demuestra lo que sabes.', max_length=255)),
                ('fecha_creacion', models.DateField(default=django.utils.timezone.now)),
                ('puntos', models.SmallIntegerField(default=150)),
                ('miniatura', models.ImageField(upload_to='images/miniaturas/')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.curso')),
            ],
        ),
        migrations.AddField(
            model_name='pregunta',
            name='cuestionario',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='cursos.cuestionario'),
            preserve_default=False,
        ),
    ]