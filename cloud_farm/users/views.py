# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from models import Users
from supplier.models import Product,Suppliers,Order
import hashlib 
from django.contrib import auth 
# Create your views here.
def  home(request):
	return render(request,'users/home.html')

def register(request):
	# print "fffffffffffffffff"
	if request.method == "POST":
		# print "fvrgf";
		name=request.POST.get('name','')
		address=request.POST.get('address','')
		mobile=request.POST.get('mobile','')
		mail=request.POST.get('email','')  
		pswd=request.POST.get('password','') 
		uname=request.POST.get('uname','') 
		b = Users(name=name,address=address,mobile=mobile,email=mail,password=pswd,uname=uname)
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
			for x in r:
				request.session['id']=x.id
			p=Product.objects.all().filter(Quantity__gte=1)
			k=Suppliers.objects.all()
			return render(request,'users/start.html',{'data':p,'y':k})
		else:
			return render(request,'users/login.html',{'er_msg':'Invalid username or password'})
	return render(request,'users/login.html')

def order(request):
	p=Product.objects.all().filter(Quantity__gte=1)
	k=Suppliers.objects.all()
	return render(request,'users/start.html',{'data':p,'y':k})

def logout(request):
	auth.logout(request)

	
	return HttpResponseRedirect('/user')
def morder(request):
	a=request.GET.get('pid','')
	c=request.GET.get('sid','')
	print c
	b=Product.objects.all().filter(id=a)
	return render(request,"users/backuporder.html",{'data':b,'sid':c})

def mkorder(request):
	if request.method=='POST':
		a=request.session['id']
		z=Users.objects.get(id=a)
		b=request.POST.get('Supplierid','')
		print b
		y=Suppliers.objects.get(id=b)
		print "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
		print b
		c=request.POST.get('productid','')
		x=Product.objects.get(id=c)
		print c
		print x.Quantity

		d=request.POST.get('quantity','')
		print d
		r=Order.objects.all().filter(SID=b,PID=c,UID=a,Status=0)
		if r.exists():
			s="Already Ordered"
			p=Product.objects.all()
			k=Suppliers.objects.all()
			return render(request,'users/start.html',{'data':p,'y':k,'z':s})
		else:
			print "---------------------------------------"
			if int(x.Quantity)<=int(d):
				print "*************************"
				s="Out Of Stock"
				p=Product.objects.all()
				k=Suppliers.objects.all()
				return render(request,'users/start.html',{'data':p,'y':k,'z':s})
			else:
				print "++++++++++++++++++++++++++++++++++++++++++"
				
				ob=Order(SID=y,PID=x,UID=z,Quantity=d)
				ob.save()
			s="Order Success"	
			p=Product.objects.all()
			k=Suppliers.objects.all()
			return render(request,'users/start.html',{'data':p,'y':k,'z':s})


	else:
		a=request.GET.get('pid','')
		c=request.GET.get('sid','')
		print c
		b=Product.objects.all().filter(id=a)
		return render(request,"users/order.html",{'data':b,'sid':c})		


def my_order(request):
	a=request.session['id']
	print "id--------------->"+str(a)
	b=Order.objects.select_related('SID').select_related('PID').filter(UID=a,Status=1)
	
	print b.query
	
	return render(request,"users/myorder.html",{'data':b})


def finds(request):
	p=request.GET.get('val','')	
	print "sssssssssssssssssssssssssssssssssssssssssssssssssss"
	print p
	if p=="1":
		a=Product.objects.all().filter(Catogory="Fruit")
		print a
	elif p=="2":
		a=Product.objects.all().filter(Catogory="Grain")
	elif p=="3":
		a=Product.objects.all().filter(Catogory="Vegitables")	
	print a
	html=""
	for x in a:
		html +="<div class='grid1_of_4'><div class='content_box'><a href='details.html'><img src="+x.Photo.url+" class='img-responsive' style='height:150px; width:200px' alt='/> </a><h4><a href='View_one_product1.php?id=9'> Quick View</a></h4><p>"+x.Name +"</p><div class='grid_1 simpleCart_shelfItem'><div class='item_add'><span class='item_price'><h6>ONLY Rs."+ x.Price +"</h6></span></div><div class='item_add'><span class='item_price'><a href='' >Buy Now</a></span></div></div></div></div>"
	return HttpResponse(html)
	

def search(request):
	s=request.POST.get('srch',"")
	print s
	n=Product.objects.all().filter(Name=s)
	return render(request,"users/start.html",{'data':n})


def total(request):
	d=request.GET.get('valu',None)
	f=request.GET.get('pric',None)
	r=int(d)*int(f)
	print r
	
	return HttpResponse(r)


def pending(request):
	a=request.session['id']
	print "id--------------->"+str(a)
	b=Order.objects.select_related('SID').select_related('PID').filter(UID=a,Status=0)
	
	
	return render(request,"users/myorder.html",{'data':b})

def Ordered(request):
	a=request.session['id']
	c=request.GET.get('pid','')
	print c
	b=Order.objects.select_related('SID').filter(UID=a,PID=c)
	return render(request,"users/viewp.html",{'data':b})
