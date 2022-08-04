# Generated by Django 4.0.6 on 2022-08-04 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('horas', models.CharField(max_length=2)),
                ('creditos', models.CharField(max_length=2)),
                ('Fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
    ]
