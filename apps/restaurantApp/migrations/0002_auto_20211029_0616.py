# Generated by Django 2.2.4 on 2021-10-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='nro_mesa',
            field=models.CharField(max_length=5, unique=True, verbose_name='Mesa'),
        ),
    ]
