# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-01 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0006_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Status',
            field=models.IntegerField(default='0'),
        ),
    ]
