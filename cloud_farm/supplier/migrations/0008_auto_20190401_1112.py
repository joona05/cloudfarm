# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-01 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0007_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Quantity',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Quantity',
            field=models.IntegerField(default='0'),
        ),
    ]