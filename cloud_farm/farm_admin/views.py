# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Admin_login
from supplier.models import Suppliers,Product
from users.models import Users
# Create your views here.
def admin_login(request):
	if request.method == "POST":
		uname=request.POST.get('username','')
		passwrd=request.POST.get('password','')
		print uname
		print passwrd
		# print hashlib.md5(passwrd)
		r=Admin_login.objects.all().filter(username=uname,password=passwrd)
		print r
		if r.exists():
			for x in r:
				request.session['id']=x.id
			return render(request,'admin/dashboard.html')
		else:
			return render(request,'admin/login.html',{'er_msg':'Invalid username or password'})
	return render(request,'admin/login.html')


def unaprove(request):
	u= Suppliers.objects.all().filter(action=0)	
	return render(request,"admin/APsuppier.html",{'data':u})

def aprove(request)	:
	u= Suppliers.objects.all().filter(action=1)	
	return render(request,"admin/supplier.html",{'data':u})

def conform(request):
	id=request.GET.get('id','')
	Suppliers.objects.filter(id=id).update(action=1)	
	u= Suppliers.objects.all().filter(action=0)	
	return render(request,"admin/APsuppier.html",{'data':u})


def product(request):
	q=Product.objects.all()
	return render(request,"admin/product.html",{'data':q})
def user(request):
	n=Users.objects.all()
	return render(request,"admin/user.html",{'data':n})	


def chpsw(request):
	if request.method=="POST":
		c=request.POST.get('password','')
		d=request.POST.get('password1','')
		if c==d:
			e="Password Change Success"
			f=Admin_login.objects.update(password=c)
			return render(request,"admin/login.html",{'n':e})
		else:
			g="Incorrect Password"	
			return render(request,"admin/psw.html",{'m':g})	

	else:
		a=request.session['id']
		b=Admin_login.objects.all().filter(id=a)
		return render(request,"admin/psw.html",{'data':b})	
