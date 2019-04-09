# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-21 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('mobile', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=30)),
                ('location', models.CharField(default='', max_length=30)),
                ('license', models.CharField(default='', max_length=30)),
                ('GST_Number', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=30)),
                ('uname', models.CharField(default='', max_length=30)),
                ('action', models.IntegerField(default='0')),
            ],
        ),
    ]
