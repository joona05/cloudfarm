# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Admin_login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)