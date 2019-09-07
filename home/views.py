# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Blogger

def mainpage(request):
	blogger=Blogger.objects.filter(username=request.user.username)
	if len(blogger)>0:
		blogger_check=False
	else:
		blogger_check=True
	return render(request,"home/homepage.html",{'blogger':blogger_check})

def about_us(request):
	return render(request,"home/about_us.html")

def contact_us(request):
	return render(request,"home/contact_us.html")
