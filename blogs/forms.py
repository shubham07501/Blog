from django import forms
from .models import Post,Comment,Blogger

class Post_Form(forms.ModelForm):
	title=forms.CharField(max_length=40)
	text=forms.CharField(max_length=2000)
	class Meta:
		model=Post
		fields=('title', 'text')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class Register_Blogger(forms.ModelForm):
	name=forms.CharField(max_length=30)
	description=forms.CharField(max_length=2000)
	email=forms.EmailField()
	class Meta:
		model=Blogger
		fields=('name','description','email','image','insta','fb','twitter',)