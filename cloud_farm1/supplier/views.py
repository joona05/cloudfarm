# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect
from models import Suppliers,Product,Order

from forms import pic
import hashlib
from django.contrib import auth 
from django.core.urlresolvers import reverse
# Create your views here.
def  home(request):
	return render(request,'supplier/shome.html')

def supplier_register(request):
	if request.method == "POST":
		# print "fvrgf";
		name=request.POST.get('name','')
		mobile=request.POST.get('mobile','')
		mail=request.POST.get('email','')  
		location=request.POST.get('location','') 
		license=request.POST.get('license','') 
		GST_Number=request.POST.get('GST_Number','') 
		pswd=request.POST.get('password','') 
		uname=request.POST.get('uname','') 
		r=Suppliers.objects.all().filter(email=mail,password=pswd)
		if r.exists():
			return render(request,'supplier/sregister.html',{'msg':'Already Exist'})
			
		else:
			b = Suppliers(name=name,mobile=mobile,email=mail,location=location,license=license,GST_Number=GST_Number,password=pswd,uname=uname)
			b.save()
			return render(request,'supplier/slogin.html',{'msg':'Registration Success'})
	# print "dffffffffff---------------------------------"
	return render(request,'supplier/sregister.html')


def login(request):
	if request.method == "POST":
		uname=request.POST.get('username','')
		passwrd=request.POST.get('password','')
		print uname
		print passwrd
		print hashlib.md5(passwrd)
		r=Suppliers.objects.all().filter(uname=uname,password=passwrd,action=1)
		print r
		if r.exists():
			for x in r:
				request.session['id']=x.id
			return render(request,'supplier/product.html')
		else:
			return render(request,'supplier/slogin.html',{'er_msg':'Invalid username or password or not approved by admin'})
	return render(request,'supplier/slogin.html')	

def add(request):
	if request.session['id']=="":
		return HttpResponseRedirect(reverse('/supplier/logload/'))
	else:	

			if request.method== "POST":
				a=request.session['id']
				print a
				name=request.POST.get('productname','')
				description=request.POST.get('description','')
				price=request.POST.get('price','')
				oprice=request.POST.get('oldprice','')
				quantity=request.POST.get('quantity','')
				catogory=request.POST.get('catogory','')
				r=Product.objects.all().filter(Name=name)
				profileform=pic(request.POST,request.FILES)
				print profileform
				if profileform.is_valid():
					# ob=Photos()
					Photo=profileform.cleaned_data['Photo']
					# q=Product.objects.get(id=a)
					# print q
					# ob.Product_id=q
					# Photos.objects.filter(Product_id=a).delete()
					# ob.save()
				if r.exists():
					return render(request,'supplier/product.html',{'msg':'Already Exist'})
					
				else:
					ob=Product(Name=name,Description=description,Price=price,Old_Price=oprice,Quantity=quantity,Catogory=catogory,SupplierID=a,Photo=Photo)
					ob.save()
					q=Product.objects.all()
					return render(request,"supplier/details.html",{'data':q})
			else:
				return render(request,'supplier/product.html')
		
def logout(request):
	print "ssssssssssss"
	print request.session['id']
	auth.logout(request)

	# i=request.session['id']
	# del request.session['id']
	# print i
	# request.session['id']==""
	return HttpResponseRedirect('/supplier')


def product(request):
	if request.session['id']=='':
		return HttpResponseRedirect(reverse('/supplier/logload/'))

	else:
		q=Product.objects.all()
		# r=Photos.objects.all
		return render(request,"supplier/details.html",{'data':q})


# def addpho(request):
# 	i=request.session['id']
# 	p=Photos.objects.all().filter(Product_id=i)
# 	return render(request,"supplier/photo.html",{'c':p})


# def photo(request):
# 	a=request.session['id']
# 	print a
	
		# edit()
	
 	# q=emppost.objects.all().filter(EmpID=EmpID)
 	# v=Photos.objects.all().filter(EmpID=EmpID)
 	# print v
 	# b=Resume.objects.all().filter(EmpID=EmpID)
 	# return render(request,'supplier/product.html',{'msg':'Photo Added'})


def edit(request):
	a=request.GET.get('pid','')
	q=Product.objects.all().filter(id=a)
	print q
	

	return render(request,"supplier/update.html",{'data':q})	

def update(request):
	if request.method== "POST":
		a=request.session['id']
		print a
		i=request.POST.get('id','')
		name=request.POST.get('productname','')
		description=request.POST.get('description','')
		price=request.POST.get('price','')
		oprice=request.POST.get('oldprice','')
		quantity=request.POST.get('quantity','')
		catogory=request.POST.get('catogory','')
		r=Product.objects.all().filter(Name=name)
		profileform=pic(request.POST,request.FILES)
		print profileform
		if profileform.is_valid():
			Photo=profileform.cleaned_data['Photo']
					
				# if r.exists():
				# 	return render(request,'supplier/product.html',{'msg':'Already Exist'})
					
				# else:
		Product.objects.filter(id=i).update(Name=name,Description=description,Price=price,Old_Price=oprice,Quantity=quantity,Catogory=catogory,SupplierID=a,Photo=Photo)
	
		q=Product.objects.all()
		return render(request,"supplier/details.html",{'data':q})
	# else:
	# 	return render(request,'supplier/product.html')
 # 

def search(request):
	s=request.POST.get('srch',"")
	print s
	n=Product.objects.all().filter(Name=s)
	return render(request,"supplier/details.html",{'data':n}) 

def Orderlist(request):
	a=request.session['id']
	a1=Order.objects.select_related('UID').select_related('PID').filter(SID=a,Status=0)
	# for x in a1:
	# 	print x.SID.name

		
	return render(request,"supplier/orderlist.html",{'data':a1})

def Orderedlist(request):
	a=request.session['id']
	a1=Order.objects.select_related('UID').select_related('PID').filter(SID=a,Status=1)
	
	# for x in a1:
	# 	print x.SID.name

		
	return render(request,"supplier/orderedlist.html",{'data':a1})



def approve(request):
	a=request.GET.get('id','')
	v=request.session['id']
	c=request.GET.get('name','')
	b=request.GET.get('Quantity','')
	e=Order.objects.select_related('PID').filter(id=a)
	for x in e:
		f=x.PID.Quantity
		
	print f
	print b
	if int(f)<int(b):
		print "___________________________"
		n="Out Of Stock"
		a1=Order.objects.select_related('UID').select_related('PID').filter(SID=v,Status=0)
		return render(request,"supplier/orderlist.html",{'data':a1,'z':n})
		
	else:
		print "+++++++++++++++++++++++++++++++++++++++"	
		g=int(f)-int(b)
		d=Product.objects.filter(Name=c).update(Quantity=g)
		q=Order.objects.filter(id=a).update(Status=1)

	
	print   
	a1=Order.objects.select_related('UID').select_related('PID').filter(SID=v,Status=0)
	return render(request,"supplier/orderlist.html",{'data':a1})

				