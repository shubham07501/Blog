# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Blogger(models.Model):
	username=models.CharField(max_length=30,null=True,default=None)
	blogger_name=models.CharField(max_length=30,default=None,null=True)
	blogger_desc=models.TextField()
	blogger_email=models.CharField(max_length=40,null=True)
	image=models.ImageField(upload_to='profile_image',null=True)
	insta=models.URLField(max_length=100,null=True,blank=True)
	fb=models.URLField(max_length=100,null=True,blank=True)
	twitter=models.URLField(max_length=100,null=True,blank=True)
	def __str__(self):
		return self.blogger_name

class Post(models.Model):
	blogger=models.ForeignKey(Blogger,on_delete=models.CASCADE)
	post_title=models.CharField(max_length=100)
	post_detail=models.TextField()
	pub_date=models.DateTimeField('date published',null=True)	
	def __str__(self):
		return self.post_title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments',null=True)
    author = models.CharField(max_length=200,null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now,null=True)
    def __str__(self):
    	return self.text