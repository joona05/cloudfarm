# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import Users

# Create your models here.
class Suppliers(models.Model):
    name=models.CharField(max_length=30,default='')
    mobile=models.CharField(max_length=30,default='')
    email=models.CharField(max_length=30,default='')
    location=models.CharField(max_length=30,default='')
    license=models.CharField(max_length=30,default='')
    GST_Number=models.CharField(max_length=30,default='')
    password=models.CharField(max_length=30,default='')
    uname=models.CharField(max_length=30,default='')
    action=models.IntegerField(default='0')

class Product(models.Model):
	Name=models.CharField(max_length=30,default='')
	Description=models.CharField(max_length=50,default='')
	Price=models.CharField(max_length=30,default='')
	Old_Price=models.CharField(max_length=30,default='')
	Quantity=models.IntegerField(default='0')
	Catogory=models.CharField(max_length=30,default='')
	SupplierID=models.CharField(max_length=30,default='')
	Photo=models.ImageField(upload_to = 'user_images',default='')



class Order(models.Model):
	SID=models.ForeignKey(Suppliers,default='')	
	PID=models.ForeignKey(Product,default='')
	UID=models.ForeignKey(Users,default='')
	Quantity=models.IntegerField(default='0')
	Status=models.IntegerField(default='0')
