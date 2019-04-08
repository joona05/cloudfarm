# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Admin_login
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
			return render(request,'admin/dashboard.html')
		else:
			return render(request,'admin/login.html',{'er_msg':'Invalid username or password'})
	return render(request,'admin/login.html')
	