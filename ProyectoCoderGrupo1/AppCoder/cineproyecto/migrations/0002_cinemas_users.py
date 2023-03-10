# Generated by Django 4.0.3 on 2022-04-03 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cineproyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('address', models.CharField(max_length=30, verbose_name='Dirección')),
                ('num_of_seats', models.IntegerField(verbose_name='Capacidad')),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, verbose_name='Telefono')),
                ('other_info', models.CharField(max_length=30, verbose_name='Otros datos')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('surname', models.CharField(max_length=30, verbose_name='Apellido')),
                ('user_name', models.CharField(max_length=30, unique=True, verbose_name='Nombre de usuario')),
                ('password', models.CharField(max_length=30, verbose_name='Contraseña')),
                ('mail', models.EmailField(max_length=254)),
                ('birth_date', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('other_info', models.CharField(max_length=30, verbose_name='Otros datos')),
            ],
        ),
    ]
