# Generated by Django 3.2.6 on 2021-10-17 22:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0004_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.TimeField(default=datetime.datetime),
        ),
    ]