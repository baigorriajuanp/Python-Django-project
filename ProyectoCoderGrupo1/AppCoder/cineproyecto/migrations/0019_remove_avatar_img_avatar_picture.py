# Generated by Django 4.0.3 on 2022-04-24 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cineproyecto', '0018_alter_blogs_img_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='img',
        ),
        migrations.AddField(
            model_name='avatar',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]