# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-25 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_product_supplierid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='Product_id',
        ),
        migrations.AddField(
            model_name='product',
            name='Photo',
            field=models.ImageField(default='', upload_to='user_images'),
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
    ]
