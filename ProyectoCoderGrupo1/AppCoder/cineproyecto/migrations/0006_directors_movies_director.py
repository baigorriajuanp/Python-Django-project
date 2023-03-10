# Generated by Django 4.0.3 on 2022-04-17 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cineproyecto', '0005_actors_movies_actor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('surname', models.CharField(max_length=30, verbose_name='Apellido')),
                ('nac', models.CharField(max_length=30, verbose_name='Nacionalidad')),
                ('birth_date', models.DateField(verbose_name='Nacimiento')),
            ],
        ),
        migrations.AddField(
            model_name='movies',
            name='director',
            field=models.ManyToManyField(to='cineproyecto.directors'),
        ),
    ]
