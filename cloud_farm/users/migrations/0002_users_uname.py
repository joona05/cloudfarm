# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-15 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='uname',
            field=models.CharField(default='a', max_length=30),
            preserve_default=False,
        ),
    ]
