# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-09-06 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200906_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=6, max_digits=18),
        ),
    ]