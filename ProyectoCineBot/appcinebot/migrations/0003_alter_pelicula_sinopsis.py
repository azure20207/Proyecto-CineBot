# Generated by Django 4.0.4 on 2022-04-28 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcinebot', '0002_pelicula_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='sinopsis',
            field=models.CharField(max_length=200),
        ),
    ]
