# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post,Blogger,Comment
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from .forms import CommentForm,Register_Blogger,Post_Form
from django.utils import timezone
from django.contrib.auth.models import User


def blogs_show_all(request):
    blogger=Blogger.objects.filter(username=request.user.username)
    if blogger:
        blogger=blogger[0]
    blogs_list=Post.objects.order_by('-pub_date')[:]
    paginator=Paginator(blogs_list,5)
    page=request.GET.get('page',1)
    blogs=paginator.page(page)
    return render(request,'blogs/blogs_page.html',{'blog_list':blogs,'blogger':blogger})


def all_bloggers(request):
    bloggers_list=Blogger.objects.order_by('blogger_name')
    return render(request,'blogs/all_bloggers.html',{'bloggers_list':bloggers_list})    

def blogger_detail(request,author_id):
    blog=Post.objects.order_by('-pub_date')[:]
    blogger=get_object_or_404(Blogger, pk=author_id)
    return render(request,"blogs/blogger_detail.html",{'blogger':blogger,'blog':blog})

def blog_details(request,blog_id):
    blog=get_object_or_404(Post, pk=blog_id)
    comment=Comment.objects.filter(post=blog)
    return render(request,"blogs/blog_details.html",{'blog':blog,'comment':comment})

def user_login(request):
    return HttpResponseRedirect('/login/')

def user_logout(request):
    return HttpResponseRedirect('/logout/')

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(request,username=username,password=raw_password)
            login(request,user)
            return redirect('/blog/blogs/')
    else:
        form=UserCreationForm()
    return render(request,'blogs/signup.html',{'form':form})

def user_authentication(request):
    user=None
    return render(request,"home/homepage.html",{'user':user})


def add_comment_to_post(request, blog_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(request.POST)
            
            if form.is_valid():
                comment=form.save()
                comment.post=get_object_or_404(Post,id=blog_id)
                comment.author=request.user.username
                comment.text=form.cleaned_data.get('text')
                comment=form.save()
                return redirect('blogs:details',blog_id)
        else:
            form = CommentForm()
        return render(request, 'blogs/add_comment_to_post.html', {'form': form})
    else:
        return redirect("home:main")


def register_blogger(request):
    if request.user.is_authenticated():
        if request.method=='POST':
            form=Register_Blogger(request.POST,request.FILES)
            blogger=Blogger()
            if form.is_valid():
                blogger.username=request.user.username
                blogger.blogger_name=form.cleaned_data['name']
                blogger.blogger_desc=form.cleaned_data['description']
                blogger.blogger_email=form.cleaned_data['email']
                blogger.insta=form.cleaned_data['insta']
                blogger.fb=form.cleaned_data['fb']
                blogger.twitter=form.cleaned_data['twitter']
                blogger.save()
                return redirect('blogs:all_bloggers')
        else:
            form=Register_Blogger()
        return render(request,'blogs/register_blogger.html',{'form':form})
    else:
        return redirect("/login/")


    
def add_post(request):
    if request.user.is_authenticated():
        if request.method=="POST":
            form=Post_Form(request.POST)
            blog = Post()
            blogger=Blogger.objects.filter(username=request.user.username)
            if form.is_valid():
                blog.blogger=blogger[0]
                blog.post_title=form.cleaned_data['title']
                blog.post_detail=form.cleaned_data['text']
                blog.pub_date=timezone.now()
                blog.save()
                return redirect ('blogs:show_all')
        else:
            form=Post_Form()
        return render(request,'blogs/add_post.html',{'form':form})
    else:
        return redirect("/login/")


def log_me_out(request):
    logout(request)
    return HttpResponseRedirect('/blog')