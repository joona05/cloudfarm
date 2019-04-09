# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=30,default='')
    address=models.CharField(max_length=50,default='')
    mobile=models.CharField(max_length=30,default='')
    email=models.CharField(max_length=30,default='')
    password=models.CharField(max_length=30,default='')
    uname=models.CharField(max_length=30,default='')
    
    
