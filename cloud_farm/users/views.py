# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Users
import hashlib 
# Create your views here.
def  home(request):
	return render(request,'users/home.html')

def register(request):
	# print "fffffffffffffffff"
	if request.method == "POST":
		# print "fvrgf";
		name=request.POST.get('name','')
		mobile=request.POST.get('mobile','')
		mail=request.POST.get('email','')  
		pswd=request.POST.get('password','') 
		uname=request.POST.get('uname','') 
		b = Users(name=name,mobile=mobile,email=mail,password=pswd,uname=uname)
		b.save()
		return render(request,'users/register.html',{'msg':'Registration Success'})
	# print "dffffffffff---------------------------------"
	return render(request,'users/register.html')

def login(request):
	if request.method == "POST":
		uname=request.POST.get('username','')
		passwrd=request.POST.get('password','')
		print uname
		print passwrd
		print hashlib.md5(passwrd)
		r=Users.objects.all().filter(uname=uname,password=passwrd)
		print r
		if r.exists():
			return render(request,'users/home.html')
		else:
			return render(request,'users/login.html',{'er_msg':'Invalid username or password'})
	return render(request,'users/login.html')
